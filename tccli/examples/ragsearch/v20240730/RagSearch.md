**Example 1: RagSearch-NonStream**

RagSearch

Input: 

```
tccli ragsearch RagSearch --cli-unfold-argument  \
    --Query What sutras did Sakyamuni write \
    --WorkFlowId flow-okbt9fh8
```

Output: 
```
{
    "Response": {
        "Created": 1723023402,
        "Note": "",
        "Choices": [
            {
                "FinishReason": "stop",
                "Message": {
                    "Role": "assistant",
                    "Content": "Sakyamuni wrote many sutras, but the specific document provided does not contain the information needed to answer your question. If you have access to a comprehensive collection of Buddhist scriptures, you may find a list of sutras attributed to Sakyamuni there."
                }
            }
        ],
        "RequestId": "8cdb8fe0-54a0-11ef-af25-525400cb110a"
    }
}
```

**Example 2: NoAnswerResponse**

NoAnswerResponse

Input: 

```
tccli ragsearch RagSearch --cli-unfold-argument  \
    --Query p.2223 \
    --WorkFlowId flow-okbt9fh8
```

Output: 
```
{
    "Response": {
        "Created": 1723693346,
        "Id": "85307482-4686-46a4-bd8a-0fa78dd906f9",
        "Choices": [
            {
                "FinishReason": "stop",
                "Message": {
                    "Role": "assistant",
                    "Content": "抱歉，根据现有的文档内容无法回答这一问题。"
                }
            }
        ],
        "RequestId": "85307482-4686-46a4-bd8a-0fa78dd906f9"
    }
}
```

