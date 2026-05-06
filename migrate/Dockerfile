FROM python:3.12-slim

# Install runtime deps first so the layer caches well.
WORKDIR /src/migrate
COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt

# The script itself is bind-mounted at runtime by docker-compose, so we don't
# COPY it here — that way edits show up without rebuilding the image.
# (If you'd rather bake it in, uncomment the next line.)
# COPY migrate_drupal.py /src/migrate/migrate_drupal.py

# Run as a non-root user so files written into the bind mount end up with
# sane ownership on the host.
ARG UID=1000
ARG GID=1000
RUN groupadd -g ${GID} app && useradd -m -u ${UID} -g ${GID} app
USER app
