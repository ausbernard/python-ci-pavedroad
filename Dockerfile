FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONPATH=/app/src

# Create and set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt && \
    rm -rf /root/.cache/pip

# Copy application code
COPY src/ src/

# Create non-root user
RUN useradd -m appuser && chown -R appuser:appuser /app
USER appuser

# Add entry point as shell
ENTRYPOINT ["/bin/sh", "-c"]

# Run the application
CMD ["uvicorn", "python_ci_pavedroad_template_app.app:app", "--host", "0.0.0.0", "--port", "8080"]
