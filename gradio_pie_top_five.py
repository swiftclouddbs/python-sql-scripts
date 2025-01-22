import gradio as gr
import pandas as pd
import matplotlib.pyplot as plt
import tempfile

def generate_pie_chart(file):
    try:
        # Read the uploaded CSV
        df = pd.read_csv(file)
        
        # Ensure the CSV has exactly one column
        if df.shape[1] != 1:
            return None, "Error: The uploaded CSV must have exactly one column of data."
        
        # Extract the single column
        column = df.iloc[:, 0]
        
        # Compute the top 5 most frequent values
        top_five = column.value_counts().head(5)
        
        # Generate the pie chart
        plt.figure(figsize=(8, 6))
        plt.pie(
            top_five.values,
            labels=top_five.index.astype(str),
            autopct='%1.1f%%',
            startangle=140,
            colors=plt.cm.tab10.colors
        )
        plt.title("Top 5 Most Frequent Values", fontsize=14)
        
        # Save the pie chart to a temporary file
        temp_image_path = tempfile.mktemp(suffix=".png")
        plt.savefig(temp_image_path)
        plt.close()
        
        return temp_image_path, "Pie chart generated successfully."
    except Exception as e:
        return None, f"Error: {e}"

# Gradio interface
with gr.Blocks() as app:
    gr.Markdown("### Drag and Drop a CSV File to Create a Pie Chart")
    
    csv_input = gr.File(label="Upload CSV File", file_types=[".csv"])
    graph_output = gr.Image(label="Pie Chart")
    status_output = gr.Textbox(label="Status", interactive=False)
    
    generate_button = gr.Button("Generate Pie Chart")
    
    generate_button.click(
        generate_pie_chart,
        inputs=[csv_input],
        outputs=[graph_output, status_output]
    )

app.launch(server_name="0.0.0.0", server_port=7863)
