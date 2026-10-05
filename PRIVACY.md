# Privacy Policy

## What this plugin sends

When a tool is invoked, the plugin sends to `https://saymaker.ai`:

- the prompt text you or your workflow supplied
- for edits and image-to-video, the image URL you supplied
- your SayMaker API key, as a Bearer token, to authenticate the run

Nothing else leaves the plugin.

## What this plugin stores

Nothing. The API key is held by Dify's credential storage, not by the plugin, and the plugin keeps no state between calls.

## What the service does with it

Prompts and generated files are processed by SayMaker to produce the result and are served from SayMaker's CDN at a public URL; treat that URL as public. Each run is recorded in your SayMaker history and charged to your account like a run on the site. SayMaker's terms and privacy policy apply: <https://saymaker.ai/privacy-policy>

## Contact

<https://github.com/hanshs474/saymaker-dify-plugin/issues>
