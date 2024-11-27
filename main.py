import gradio as gr
import requests
import subprocess
import matplotlib.pyplot as plt
import io
import base64
import os

API_URL = "https://ai.api.nvidia.com/v1/vlm/nvidia/neva-22b"
API_KEY = "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"

def trim_video(video_path, start_time, end_time):
    trimmed_path = f"{os.path.splitext(video_path)[0]}_trimmed.mp4"
    command = [
        "ffmpeg", "-i", video_path,
        "-ss", str(start_time), "-to", str(end_time),
        "-c:v", "libx264", "-c:a", "aac", "-strict", "experimental",
        trimmed_path
    ]
    subprocess.run(command, check=True)
    return trimmed_path

def detect_action(action):
    # Prepare the payload with only the action as message
    payload = {
        "messages": [
            {
                "role": "user",
                "content": action  # Action to detect, e.g., "jumping"
            }
        ]
    }

    # Prepare the headers
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    # Make the API request
    response = requests.post(API_URL, headers=headers, json=payload)

    # Debug: Print the API response for debugging purposes
    print("API Response (Status Code):", response.status_code)
    print("API Response (Text):", response.text)

    # Check for success or failure
    if response.status_code == 200:
        result = response.json()
        print("Result JSON:", result)  # Debugging: Check the response structure
        # Check if success_rate is in the result
        if "success_rate" in result:
            success_rate = result["success_rate"]
        else:
            success_rate = "No success_rate in response"
        return success_rate
    else:
        return f"Error: {response.status_code} - {response.text}"

def plot_success_rates(real_rate, synthetic_rate):
    fig, ax = plt.subplots()
    ax.bar(["Real Video", "Synthetic Video"], [real_rate, synthetic_rate], color=["blue", "orange"])
    ax.set_ylim(0, 100)
    ax.set_ylabel("Success Rate (%)")
    ax.set_title("Action Recognition Success Rates")

    buf = io.BytesIO()
    plt.savefig(buf, format="png")
    buf.seek(0)
    plt.close(fig)

    img_str = base64.b64encode(buf.read()).decode("utf-8")
    return f"data:image/png;base64,{img_str}"

def process_videos(real_video, synthetic_video, start1, end1, start2, end2, action):
    # Trim videos first
    trimmed_real = trim_video(real_video, start1, end1)
    trimmed_synthetic = trim_video(synthetic_video, start2, end2)

    # Detect actions and calculate success rates
    success_rate_real = detect_action(action)
    success_rate_synthetic = detect_action(action)

    # Generate success rate plot
    plot_url = plot_success_rates(success_rate_real, success_rate_synthetic)

    try:
        os.remove(trimmed_real)
        os.remove(trimmed_synthetic)
    except OSError as e:
        print(f"Error removing file: {e}")

    return f"Real Video Success Rate: {success_rate_real}%", f"Synthetic Video Success Rate: {success_rate_synthetic}%", plot_url

# Gradio Interface
interface = gr.Interface(
    fn=process_videos,
    inputs=[
        gr.Video(label="Upload Real Video"),
        gr.Video(label="Upload Synthetic Video"),
        gr.Slider(0, 60, step=1, label="Real Video - Start Time"),
        gr.Slider(0, 60, step=1, label="Real Video - End Time"),
        gr.Slider(0, 60, step=1, label="Synthetic Video - Start Time"),
        gr.Slider(0, 60, step=1, label="Synthetic Video - End Time"),
        gr.Textbox(label="Specify Action to Detect", placeholder="e.g., jumping"),
    ],
    outputs=[
        gr.Textbox(label="Real Video Success Rate"),
        gr.Textbox(label="Synthetic Video Success Rate"),
        gr.Image(label="Success Rate Comparison"),
    ],
    title="Action Recognition Comparison",
    description="Upload two videos, trim them, and detect specified actions using NVIDIA VLM.",
)

if _name_ == "_main_":
    interface.launch(share=True)