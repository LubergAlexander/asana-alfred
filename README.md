# Intro
Haven't found a working Asana-Alfred extension, so built this one. It creates tasks in a predefined 'Inbox'.

# Setup

1) Set `ASANA_PERSONAL_TOKEN`, `ASANA_WORKSPACE_NAME`, `ASANA_PROJECT_NAME` in variables section.
2) make sure python from brew is installed (fresh OpenSSL is required for asana)

# Build
`lib` contains all dependencies. To install:

```bash
pip install --target=lib .
```

Then create an empty workflow in Alfred, open it's directory and replace the contents.

# Install
Install from Releases page
