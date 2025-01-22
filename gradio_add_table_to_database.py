#Add table to existing database
#

import gradio as gr
import sqlite3
import pandas as pd
import os

def add_csv_to_database(file, db_name, table_name):
    try:
        # Validate inputs
        if not file or not db_name or not table_name:
            return "Error: All inputs are required."

        # Ensure the database name ends with .db
        if not db_name.endswith(".db"):
            db_name += ".db"

        # Read the CSV file into a Pandas DataFrame
        df = pd.read_csv(file.name)

        # Connect to the SQLite database
        conn = sqlite3.connect(db_name)

        # Add the DataFrame to the database as a new table
        df.to_sql(table_name, conn, if_exists="fail", index=False)

        conn.close()
        return f"Successfully added the table '{table_name}' to the database '{db_name}'."
    except ValueError as ve:
        return f"Error: {ve}. The table might already exist. Try using a different table name."
    except Exception as e:
        return f"Error: {e}"

# Gradio interface
with gr.Blocks() as app:
    gr.Markdown("### Drag and Drop CSV to Add as Table in SQLite Database")
    
    db_input = gr.Textbox(label="Database Name (e.g., 'my_database.db')", placeholder="Enter the SQLite database name")
    table_input = gr.Textbox(label="Table Name", placeholder="Enter the name for the new table")
    csv_input = gr.File(label="Upload CSV File", file_types=[".csv"])
    status_output = gr.Textbox(label="Status", interactive=False)

    submit_button = gr.Button("Add CSV to Database")

    submit_button.click(
        add_csv_to_database,
        inputs=[csv_input, db_input, table_input],
        outputs=[status_output]
    )

app.launch(server_name="0.0.0.0", server_port=7864)
