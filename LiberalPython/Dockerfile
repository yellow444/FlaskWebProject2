FROM python:3.9
WORKDIR /app
COPY requirements.txt /app
#torch==1.9.0+cpu  -f https://download.pytorch.org/whl/torch_stable.html
RUN pip3 install torch==1.9.0+cpu torchvision==0.10.0+cpu torchaudio==0.9.0 -f https://download.pytorch.org/whl/torch_stable.html
RUN pip3 install --upgrade pip -r requirements.txt

COPY . /app
EXPOSE 5000