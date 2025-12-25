import gradio as gr
from analysis import analyze_data

def run_analysis():
    result, plot = analyze_data()

    text_output = ""
    for key, value in result.items():
        text_output += f"{key}: {value}\n"

    return text_output, plot


if __name__ == "__main__":
    app = gr.Interface(
        fn=run_analysis,
        inputs=[],
        outputs=[
            gr.Textbox(label="Analysis Result"),
            gr.Plot(label="Renewal vs Churn Bar Chart")
        ],
        title="Online Subscription Renewal Analysis",
        description="Visual analysis of subscription renewals and churn using Pandas & Matplotlib"
    )

    app.launch(share=False)