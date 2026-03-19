# Script to list all endpoints in the FinBIF API.

import json
from urllib.request import Request, urlopen

def main() -> None:
    request = Request("https://api.laji.fi/openapi-json", headers={"Accept": "application/json"})
    with urlopen(request, timeout=30) as response:
        spec = json.load(response)

    paths = spec.get("paths", {})
    for endpoint in sorted(paths.keys()):
        operations = paths.get(endpoint, {})
        for method in operations.keys():
            if method.lower() in {"get", "post", "put", "patch", "delete", "options", "head", "trace"}:
                print(f"{method.upper()} {endpoint}")


if __name__ == "__main__":
    main()