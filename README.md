# SayMaker for Dify

Generate images and video from a Dify workflow or agent on [SayMaker](https://saymaker.ai/?utm_source=dify&utm_medium=plugin): Veo 3.1, Kling 3.0, Seedance 2.0, MiniMax H3, Nano Banana 2, GPT Image 2.5 and Seedream 5.0 on one API key.

| Tool | What it does |
|---|---|
| **Generate image** | prompt (+ aspect ratio, model) to an image |
| **Edit image** | photo URL + instruction to an edited image; name what must stay |
| **Generate video** | prompt, optionally a first-frame image URL, to a clip |

Setup: create a key at [saymaker.ai/settings/apikeys](https://saymaker.ai/settings/apikeys?utm_source=dify&utm_medium=plugin) (new accounts get sign-up credits) and paste it into the provider's credentials. Runs use your account's credits and plan, exactly as on the site.

`minimax-h3-fast` is the video model a free account can run; Veo 3.1, Kling 3.0 and Seedance 2.0 need a plan or a credit pack ([pricing](https://saymaker.ai/pricing?utm_source=dify&utm_medium=plugin)). Video takes minutes, and runs on a free account wait in a queue before they start.
