FROM python:3.12.2

# Set working directory
WORKDIR /usr/src/app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0 \
    git \
    dos2unix \
    && rm -rf /var/lib/apt/lists/*

# Clone your dataset into /dataset
RUN git clone https://github.com/Omarnbl/simulator_formatted_data.git /dataset

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy your application files
COPY . .

# Create a default copy of the input config
RUN cp input_config/input_config_paramters.json input_config/input_config_paramters.json.default

# Copy entrypoint script to a global location and make it executable
COPY entrypoint.sh /usr/local/bin/entrypoint.sh
RUN chmod +x /usr/local/bin/entrypoint.sh

COPY run_app.py /usr/src/app/run_app.py
COPY load_parameters.py /usr/src/app/load_parameters.py
RUN dos2unix /usr/src/app/run_app.py /usr/src/app/load_parameters.py && \
    chmod +x /usr/src/app/run_app.py /usr/src/app/load_parameters.py && \
    ln -s /usr/src/app/run_app.py /usr/local/bin/run_app && \
    ln -s /usr/src/app/load_parameters.py /usr/local/bin/load_parameters
# Copy run_app.py to a global location and make it executable
COPY run_app.py /usr/local/bin/run_app.py
RUN chmod +x /usr/local/bin/run_app.py

# Set entrypoint
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]