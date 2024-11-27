Documentation for Human Action Recognition Workflow
This documentation outlines the setup, usage, and expected output for the Human Action Recognition Workflow built using Gradio and NVIDIA's Vision Language Model (VLM).

Overview
The application allows users to:

Upload two videos (real and synthetic) for action recognition.
Trim videos to ensure they are of similar lengths.
Detect a specified action (e.g., jumping or running) using NVIDIA's VLM.
Compare the action recognition success rates for the two videos.
Visualize the success rates using a bar chart.
Setup Instructions
Prerequisites
Python (>=3.7) installed on the machine.
FFmpeg installed for video trimming. 
NVIDIA VLM API key and endpoint URL.
Dependencies
Install the required Python libraries:

pip install gradio matplotlib requests python-dotenv

Environment Variables
Create a .env file in the project directory to store sensitive information:

plaintext
Copy code
API_URL=https://ai.api.nvidia.com/v1/vlm/nvidia/neva-22b
API_KEY=your_api_key_here



python human_action_recognition.py
This will start a local Gradio interface.

Upload Videos:

Use the file uploader to select the real and synthetic videos.
Ensure the videos are of similar lengths (trim them if necessary).
Set Trimming Times:

Use the sliders to specify start and end times for trimming each video.
For example, to analyze the first 10 seconds, set:
Start Time: 0
End Time: 10
Specify Action:

Enter the action you want the model to recognize, such as jumping, running, or walking.
Run the Workflow:

Click Submit to process the videos.
The app will:
Trim the videos.
Upload the videos to NVIDIA's VLM API for action recognition.
Display success rates for both videos and a comparison plot.
Expected Output
1. Success Rates
Real Video Success Rate: A percentage indicating how well the model detected the action in the real video.
Synthetic Video Success Rate: A percentage for the synthetic video.


Error Handling
Common Errors and Fixes

"API Error: 401 Unauthorized":
Verify your API key and endpoint in the .env file.

Demo Video
A step-by-step demo video of the workflow is uploaded as an unlisted video on YouTube. 
https://youtu.be/R-LZwsEIzQc

GitHub Repository
Structure
Code Files: Include the main script and .env.example (template for credentials).
Documentation: Include this documentation in a README.md file.


Resources
Sample Videos:

synthetic videos(provided)
Download real videos from the Charades Dataset.










