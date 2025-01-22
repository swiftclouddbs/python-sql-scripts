import gradio as gr
import sqlite3
import pandas as pd

def create_database_from_csv(file):
    try:
        # Load the CSV into a pandas DataFrame
        df = pd.read_csv(file.name)
        
        # Create SQLite database and table
        conn = sqlite3.connect("uploaded_data.db")
        df.to_sql("data", conn, if_exists="replace", index=False)
        conn.close()
        
        return f"Database created successfully with table 'data'. Rows added: {len(df)}"
    except Exception as e:
        return f"Error: {e}"

# Gradio interface
with gr.Blocks() as app:
    gr.Markdown("### Drag and Drop a CSV File to Create SQLite Database")
    file_input = gr.File(label="Upload CSV", file_types=[".csv"])
    output = gr.Textbox(label="Status")
    submit_button = gr.Button("Create Database")
    
    submit_button.click(create_database_from_csv, inputs=[file_input], outputs=[output])

app.launch(server_name="0.0.0.0", server_port=7861)
