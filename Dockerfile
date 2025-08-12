FROM node:14-slim

# Create and switch to a non-root user
RUN groupadd -r appgroup && useradd -r -g appgroup -d /app -s /sbin/nologin appuser

# Set working directory
WORKDIR /usr/src/app

# Copy package files first to cache dependencies
COPY package*.json ./

# Install dependencies securely
RUN npm ci --only=production

# Copy the rest of the application code
COPY . .

# Set permissions for the app directory
RUN chown -R appuser:appgroup /usr/src/app

# Switch to non-root user
USER appuser

# Expose port
EXPOSE 3000

# Add health check
HEALTHCHECK --interval=30s --timeout=5s --start-period=5s --retries=3 \
  CMD curl -f http://localhost:3000/health || exit 1

# Start app
CMD ["node", "server.js"]
