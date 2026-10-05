import json
import urllib.error
import urllib.request
from typing import Any

from dify_plugin import ToolProvider
from dify_plugin.errors.tool import ToolProviderCredentialValidationError


class SayMakerProvider(ToolProvider):
    def _validate_credentials(self, credentials: dict[str, Any]) -> None:
        """Check the key without starting a run.

        Polling a task id that cannot exist answers "task not found" for a valid
        key and "invalid API key" for a bad one, so nothing is queued or charged.
        """
        key = (credentials.get("api_key") or "").strip()
        if not key:
            raise ToolProviderCredentialValidationError("API key is required")
        req = urllib.request.Request(
            "https://saymaker.ai/api/ai/query",
            data=json.dumps({"taskId": "00000000-0000-0000-0000-000000000000"}).encode(),
            headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json"},
            method="POST",
        )
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                env = json.loads(r.read())
        except (urllib.error.URLError, ValueError) as e:
            raise ToolProviderCredentialValidationError(f"could not reach saymaker.ai: {e}")
        if "api key" in str(env.get("message", "")).lower():
            raise ToolProviderCredentialValidationError(env["message"])
