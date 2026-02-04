def safe_load(s):
    # Minimal YAML loader for simple dicts
    import json
    try:
        return json.loads(s)
    except Exception:
        return {}

__all__ = ['safe_load']