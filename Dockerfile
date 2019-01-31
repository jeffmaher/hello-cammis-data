FROM python:3.7

# Configurables
ENV WORK_DIR "/hello-cammis-data"
ENV APP_PORT "8000"
ENV ADDR_PORT "0.0.0.0:${APP_PORT}"

# Upgrade system packages
RUN apt-get -y -qq update && apt-get -y -qq upgrade

# Moving into the working directory
WORKDIR ${WORK_DIR}

# Copy files into the working directory
COPY . ${WORK_DIR}

# Install required Python packages
RUN pip install --no-cache-dir -r requirements.txt

# (Remove this later) Migrate the database
RUN python manage.py migrate

# Expose Port
EXPOSE ${APP_PORT}

# Run hello-cammis-data
# TODO Use ADDR_PORT here ... having trouble getting it to resolve
CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]