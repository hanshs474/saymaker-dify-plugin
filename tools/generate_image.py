from __future__ import annotations

from collections.abc import Generator
from typing import Any

from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage

from tools import _client as sm


class GenerateImageTool(Tool):
    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage]:
        prompt = (tool_parameters.get("prompt") or "").strip()
        if not prompt:
            yield self.create_text_message("prompt is required")
            return
        key = self.runtime.credentials.get("api_key")
        model = (tool_parameters.get("model") or "").strip() or None
        try:
            url = sm.generate(prompt, aspect_ratio=tool_parameters.get("aspect_ratio") or None, model=model, api_key=key)
        except sm.SayMakerError as err:
            yield self.create_text_message(f"SayMaker: {err}")
            return
        yield self.create_image_message(url)
        yield self.create_text_message(url)
