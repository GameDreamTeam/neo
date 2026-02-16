SYSTEM_PROMPT = """
You are a senior DevOps engineer assistant.
Be concise and actionable.
"""

SUMMARIZE_PROMPT = """
Summarize the following content clearly and concisely.

Content:
{content}
"""

EXPLAIN_PROMPT = """
Explain the following content simply.

Break down complex ideas.
Avoid unnecessary jargon.

Content:
{content}
"""

DEBUG_PROMPT = """
Analyze these logs and provide:

1. Root Cause
2. What Failed
3. Suggested Fix
4. Prevention Tips

Logs:
{content}
"""

FIX_PROMPT = """
Analyze the following configuration/code.

Return:

1. Issues found
2. Corrected version
3. Explanation

Content:
{content}
"""