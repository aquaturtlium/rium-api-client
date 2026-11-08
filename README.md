# RIUM API Client

A generated, typed Python client for the RIUM HTTP API. It supports synchronous and asynchronous requests and is distributed under the MIT License.

## Requirements

- Python 3.9 or newer (as constrained by the package metadata)
- Network access to the RIUM API
- An OAuth access token for operations that require authorization

The production API base URL is `https://rium-data.com/api/v1`. Consult the [RIUM API Reference](https://rium-data.com/api/v1/docs) for supported operations and access requirements.

## Installation

```sh
python -m pip install rium-api-client
```

The package is published on [PyPI](https://pypi.org/project/rium-api-client/). To install from a source checkout instead, run `python -m pip install .` from the repository root.

## Usage

Use `Client` for operations that do not require authentication and `AuthenticatedClient` with an OAuth access token for protected operations:

```python
from rium_api_client import AuthenticatedClient
from rium_api_client.api.event import get_events

client = AuthenticatedClient(
    base_url="https://rium-data.com/api/v1",
    token="YOUR_OAUTH_ACCESS_TOKEN",
)

with client:
    events = get_events.sync(client=client)
    if events is not None:
        for event in events.data:
            print(event)
```

The generated operations provide `sync`, `sync_detailed`, `asyncio`, and `asyncio_detailed` variants. Detailed calls return status, headers, content, and a parsed response where available. Keep tokens secret and leave TLS verification enabled; `verify_ssl=False` disables certificate validation.

## Development

Generation, validation, packaging, and maintenance notes for contributors are in [docs/development.md](docs/development.md).
