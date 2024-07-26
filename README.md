# LinguaBot
LinguaBot is a powerful multilingual assistant leveraging LLMs with a production-grade pipeline for text-to-text and text-to-speech translation functionalities.


# How to run the Project?

### Create a conda environment, with python>=3.10
```bash
conda create -n linguabot python=3.10 -y
```

```bash
conda activate linguabot
```


### Install the required packages
```bash
pip install -r requirements.txt
```

### Create a .env file at the root directory and add GEMINI_API_KEY
```ini
GEMINI_API_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
```

### Run the streamlit app
Running the following cmd, opens up the localhost where this app is running
```bash
streamlit run app.py
```


## How to deploy the app?
### 1. Login with your AWS console and launch an EC2 instance
### 2. Run the following commands
### Note: Do the port mapping to this port:- 8501

```bash
sudo apt-get update
```

```bash
sudo apt upgrade -y
```

```bash
sudo apt install git curl unzip tar make sudo vim wget -y
```


```bash
git clone "Your-repository"
```

```bash
sudo apt install python3-pip
```

```bash
pip3 install -r requirements.txt
```

```bash
#Temporary running
python3 -m streamlit run app.py
```

```bash
#Permanent running
nohup python3 -m streamlit run app.py
```

Note: Streamlit runs on this port: 8501