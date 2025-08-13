FROM python:3.11-alpine

# Create app directory
WORKDIR /usr/src/app

# Install build dependencies and security updates
RUN apk add --no-cache \
    gcc \
    musl-dev \
    libffi-dev \
    && pip install --upgrade pip setuptools==70.0.0 wheel

# Install Flask with pinned secure versions
RUN pip install --no-cache-dir \
    flask==3.0.2 \
    markupsafe==2.1.5 \
    itsdangerous==2.1.2 \
    werkzeug==3.0.1

# Bundle app source
COPY --chown=appuser:appgroup . .

# Create and use non-root user (optimized)
RUN addgroup -S appgroup \
    && adduser -S appuser -G appgroup \
    && chown -R appuser:appgroup /usr/src/app
USER appuser

EXPOSE 3000

HEALTHCHECK --interval=30s --timeout=10s --start-period=10s --retries=3 \
  CMD wget --no-verbose --tries=1 --spider http://localhost:3000/ || exit 1

CMD ["python", "app.py"]
