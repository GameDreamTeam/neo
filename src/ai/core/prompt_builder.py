from ai.constants.prompts import *


# ---------- GENERATE MODES ----------

def build_summarize_prompt(content: str) -> str:
    return SUMMARIZE_PROMPT.format(content=content)


def build_explain_prompt(content: str) -> str:
    return EXPLAIN_PROMPT.format(content=content)


# ---------- CHAT MODES ----------

def build_debug_messages(content: str):
    return [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": DEBUG_PROMPT.format(content=content)},
    ]


def build_fix_messages(content: str):
    return [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": FIX_PROMPT.format(content=content)},
    ]