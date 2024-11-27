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










You said:
give me a readme.md file

2/2

ChatGPT said:
ChatGPT
markdown
Copy code
# **Human Action Recognition Workflow**

This project provides a workflow for detecting human actions in videos using NVIDIA's Vision Language Model (VLM). It allows users to upload, trim, and analyze two videos (real and synthetic), compare action recognition success rates, and visualize the results.

---

## **Features**
- Upload two videos (real and synthetic).
- Trim the videos to analyze the same duration.
- Specify a human action (e.g., jumping, running) to detect.
- Calculate and display the action recognition success rates for both videos.
- Visualize success rates using a bar chart comparison.

---

## **Setup Instructions**

### **Prerequisites**
1. **Python 3.7 or higher** installed.
2. **FFmpeg** for video trimming ([Download FFmpeg](https://ffmpeg.org/download.html)).
3. NVIDIA VLM API key and endpoint URL.

### **Dependencies**
Install the required Python packages:
```bash
pip install gradio matplotlib requests python-dotenv
Environment Variables
Create a .env file in the project root to store sensitive information:

plaintext
Copy code
API_URL=https://ai.api.nvidia.com/v1/vlm/nvidia/neva-22b
API_KEY=your_api_key_here
How to Run
Clone the Repository:

bash
Copy code
git clone https://github.com/your_username/human-action-recognition.git
cd human-action-recognition
Install Dependencies:

bash
Copy code
pip install -r requirements.txt
Start the Application:

bash
Copy code
python human_action_recognition.py
Open the Interface:

Access the Gradio interface at the link provided in the terminal (e.g., http://127.0.0.1:7860).
Using the Application
Upload Videos:

Drag and drop two videos: one real and one synthetic.
Trim Videos:

Use the sliders to specify the start and end times for trimming each video.
Ensure both videos are trimmed to the same duration.
Specify Action:

Enter a human action (e.g., jumping, running) to detect.
Submit:

Click Submit to process the videos.
View Results:

Success rates for both videos.
Bar chart comparing success rates.
Expected Outputs
Success Rates:

Real Video Success Rate: e.g., 85%
Synthetic Video Success Rate: e.g., 78%
Comparison Plot:

Bar chart displaying the recognition rates for both videos.
Demo
A step-by-step demo video is available as an unlisted YouTube link. Ensure this link is shared only with the TA.

Project Structure
bash
Copy code
.
├── human_action_recognition.py    # Main application script
├── .env.example                   # Template for environment variables
├── requirements.txt               # Python dependencies
├── README.md                      # Project documentation
└── example_videos                 # Example real and synthetic video pairs
Resources
Datasets:

Download real videos: Charades Dataset
Download synthetic videos: Sims4Action Dataset
FFmpeg:

Download and install FFmpeg from FFmpeg.org.
NVIDIA VLM API:

Documentation: Refer to the official NVIDIA VLM API documentation for additional details.
Troubleshooting
Common Errors
"Error during video trimming":

Ensure FFmpeg is installed and accessible from the system PATH.
"API Error: 401 Unauthorized":

Verify the API key and endpoint in the .env file.
File Upload Issues:

Ensure uploaded files are in a valid video format.
Contributing
If you'd like to contribute:

Fork the repository.
Create a feature branch (git checkout -b feature/YourFeature).
Commit your changes (git commit -m 'Add YourFeature').
Push to the branch (git push origin feature/YourFeature).
Create a pull request.
Contact
For questions or support, contact:

TA Email: mrajendran@nvidia.com
Slack Channel: Post queries in the project Slack channel.