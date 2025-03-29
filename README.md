## Chat Sorter Engine

Imagine you have a massive history of chat messages — important and unimportant — exceeding 100,000 messages. Using a large language model (LLM) to categorize all of them can become extremely expensive.

### Why is it expensive?

To use an LLM effectively, you need to split your chat history into chunks and pass each chunk to the model for analysis. However, in order to provide proper context for each message, it's not enough to send just one message — you also need to include surrounding messages (i.e., neighbors) to help the model understand the conversation flow.

This leads to two major problems:

1. **Optimal Neighbor Count is Unknown**  
   We don’t know the ideal number of neighboring messages needed to ensure good context. The more messages we include, the better the quality — but this also significantly increases the number of chunks.

2. **Higher Cost with Increased Context**  
   Increasing the context size leads to a drastic rise in the total number of chunks, which directly increases processing cost. Categorizing tens or hundreds of thousands of messages this way becomes impractical.

---

### The Solution

This repository introduces efficient functionality that leverages structural features of chat history — such as content, timestamps, authorship, conversation threading, and message relationships — to **reduce LLM usage by up to 100x** while **improving categorization quality and accuracy**.

### Benefits

- **Dramatically lower cost**: LLM usage is minimized through intelligent pre-processing and chunk management.
- **High-quality categorization**: Even with fewer LLM calls, the results are more accurate due to better context-aware chunking.
- **Ideal for statistical analysis**: Makes large-scale message analysis feasible and cost-effective.

---

### What This Repository Offers

This codebase provides core functionality to:

- Analyze large chat histories
- Organize messages by conversation and topic
- Minimize LLM usage while maintaining or improving output quality
- Enable scalable and affordable categorization of large-scale message logs

---

With this approach, analyzing and categorizing massive chat logs becomes up to **100 times cheaper**, without sacrificing quality.

