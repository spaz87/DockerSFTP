# Use Ubuntu 20.04 as the base image
FROM ubuntu:20.04

RUN mkdir -p /keyvault

# Install SSH server
RUN apt-get update && \
    apt-get install -y openssh-server && \
    mkdir /var/run/sshd

# Configure SSH for public key authentication
RUN echo "PasswordAuthentication no" >> /etc/ssh/sshd_config && \
    echo "PubkeyAuthentication yes" >> /etc/ssh/sshd_config && \
    echo "AllowTCPForwarding no" >> /etc/ssh/sshd_config && \
    echo "PermitRootLogin no" >> /etc/ssh/sshd_config && \
    echo "ForceCommand internal-sftp" >> /etc/ssh/sshd_config

# Copy the entry point script into the container
COPY entrypoint.py /usr/local/bin/entrypoint.py
RUN chmod +x /usr/local/bin/entrypoint.py

COPY loop.py /usr/local/bin/loop.py
RUN chmod +x /usr/local/bin/loop.py

# Expose the SSH port
EXPOSE 22

# Set the entry point script as the default command
ENTRYPOINT ["/usr/local/bin/entrypoint.py"]
