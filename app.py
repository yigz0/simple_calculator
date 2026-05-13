import os
import gradio as gr

def calculate(num1, num2, operator):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        if num2 == 0:
            return "Cannot divide by zero."
        return num1 / num2


with gr.Blocks() as demo:
    gr.Markdown("# Gradio Calculator Example")
    gr.Markdown("A simple web app running on Render.")

    num1 = gr.Number(label="First Number")
    num2 = gr.Number(label="Second Number")
    operator = gr.Radio(["+", "-", "*", "/"], label="Operator")

    result = gr.Textbox(label="Result")

    button = gr.Button("Calculate")

    button.click(
        fn=calculate,
        inputs=[num1, num2, operator],
        outputs=result
    )

port = int(os.environ.get("PORT", 7860))

demo.launch(
    server_name="0.0.0.0",
    server_port=port
)