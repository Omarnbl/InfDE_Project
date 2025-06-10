FROM python:3.12.2

WORKDIR /usr/src/app

RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0 \
    git \
    dos2unix \
    && rm -rf /var/lib/apt/lists/*

RUN git clone https://github.com/Omarnbl/simulator_formatted_data.git /dataset

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

RUN cp input_config/input_config_paramters.json input_config/input_config_paramters.json.default

COPY entrypoint.sh /usr/local/bin/entrypoint.sh
RUN chmod +x /usr/local/bin/entrypoint.sh

COPY run_app.py /usr/src/app/run_app.py
COPY load_parameters.py /usr/src/app/load_parameters.py
RUN dos2unix /usr/src/app/run_app.py /usr/src/app/load_parameters.py && \
    chmod +x /usr/src/app/run_app.py /usr/src/app/load_parameters.py && \
    ln -s /usr/src/app/run_app.py /usr/local/bin/run_app && \
    ln -s /usr/src/app/load_parameters.py /usr/local/bin/load_parameters

ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]
