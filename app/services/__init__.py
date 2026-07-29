# Contains coordination and business logic.

# services/
# ├── node_service.py
# ├── execution_service.py
# ├── tool_service.py
# ├── health_service.py
# ├── heartbeat_service.py
# └── audit_service.py


# node_service.py

# Handles:

# Node identity
# Node information
# Registration details
# Agent version
# Capabilities
# execution_service.py

# Handles:

# Request execution
# Timeout handling
# Result creation
# Failure handling
# Execution duration
# Output limits
# tool_service.py

# Handles:

# Tool lookup
# Tool availability
# Tool metadata
# Tool dispatching
# health_service.py

# Checks:

# Agent health
# Docker availability
# Filesystem access
# systemd availability
# CPU and memory status
# heartbeat_service.py

# Periodically sends or exposes:

# Node status
# Last heartbeat
# Agent version
# Supported tools
# Current load
# audit_service.py

# Records:

# Tool called
# Request ID
# User or service identity
# Execution status
# Start and end times
# Policy decision
# Error details