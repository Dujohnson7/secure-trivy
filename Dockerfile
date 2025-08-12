FROM python:3.11-alpine

# Create app directory
WORKDIR /usr/src/app

# Install build dependencies
RUN apk add --no-cache gcc musl-dev libffi-dev

# Install Flask directly (no requirements.txt)
RUN pip install --no-cache-dir flask

# Bundle app source
COPY . .

# Create and use non-root user
RUN addgroup -S appgroup && adduser -S appuser -G appgroup \
    && chown -R appuser:appgroup /usr/src/app
USER appuser

EXPOSE 3000

HEALTHCHECK --interval=30s --timeout=10s --start-period=10s --retries=3 \
  CMD wget --no-verbose --tries=1 --spider http://localhost:3000/ || exit 1

CMD ["python", "app.py"]