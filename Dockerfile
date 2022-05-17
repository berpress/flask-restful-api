ENV PIP_DISABLE_PIP_VERSION_CHECK=on
RUN pip install poetry
WORKDIR /app
COPY poetry.lock pyproject.toml /app/

# 1. Install project dependencies
RUN poetry config virtualenvs.create false
RUN poetry install --no-interaction

# 2. Feature-parity with node.js base images.
RUN apt-get update && apt-get install -y --no-install-recommends git ssh

# 3. Add tools
RUN apt-get update && apt-get install -y \
curl
RUN apt-get install unzip

COPY . /app
CMD [ "python", "app.py"]
