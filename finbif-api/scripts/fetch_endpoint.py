# Script to fetch information about a specific endpoint in the FinBIF API.

import json
from urllib.request import Request, urlopen

# Change these as needed:
ENDPOINT = "/annotations"
METHOD = "get"

def main() -> None:
    request = Request("https://api.laji.fi/openapi-json", headers={"Accept": "application/json"})
    with urlopen(request, timeout=30) as response:
        spec = json.load(response)
    operation = spec["paths"][ENDPOINT][METHOD]

    info = {
        "title": spec.get("info", {}).get("title"),
        "version": spec.get("info", {}).get("version"),
        "endpoint": ENDPOINT,
        "method": METHOD.upper(),
        "summary": operation.get("summary"),
        "description": operation.get("description"),
        "parameters": operation.get("parameters", []),
        "responses": list(operation.get("responses", {}).keys()),
    }

    print(json.dumps(info, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()