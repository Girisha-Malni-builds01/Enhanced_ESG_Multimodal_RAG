
import gradio as gr
import time
from rag import answer
from metrics import log_metrics

def run_esg_query(esg_type, question):
    start = time.time()
    response = answer(f"[{esg_type}] {question}")
    latency = round(time.time() - start, 3)
    log_metrics(question, latency)
    return response, latency

with gr.Blocks(title="ESG Multimodal RAG") as demo:
    gr.Markdown("## ESG Multimodal RAG System")
    gr.Markdown("Enterprise-grade ESG Retrieval-Augmented Generation")

    esg_type = gr.Dropdown(
        choices=["Environmental", "Social", "Governance", "General"],
        label="ESG Category",
        value="General"
    )

    question = gr.Textbox(
        label="ESG Question",
        placeholder="e.g. What governance risks are disclosed?"
    )

    with gr.Row():
        submit = gr.Button("Submit", variant="primary")
        clear = gr.Button("Clear")

    answer_box = gr.Textbox(label="Answer", lines=8)
    latency_box = gr.Number(label="Latency (seconds)", precision=3)

    submit.click(
        run_esg_query,
        inputs=[esg_type, question],
        outputs=[answer_box, latency_box]
    )

    clear.click(lambda: ("", 0), outputs=[answer_box, latency_box])

demo.launch(server_name="0.0.0.0", server_port=7860)
