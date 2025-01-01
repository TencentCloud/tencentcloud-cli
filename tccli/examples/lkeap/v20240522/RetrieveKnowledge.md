**Example 1: 语义检索**

语义检索

Input: 

```
tccli lkeap RetrieveKnowledge --cli-unfold-argument  \
    --KnowledgeBaseId 49019910106 \
    --Query 国庆节放几天假 \
    --RetrievalMethod SEMANTIC \
    --RetrievalSetting.TopK 3 \
    --RetrievalSetting.ScoreThreshold 0.7
```

Output: 
```
{
    "Response": {
        "Records": [
            {
                "Metadata": {
                    "Type": "DOC",
                    "ResultSource": "SEMANTIC",
                    "ChunkPageNumbers": [
                        1
                    ]
                },
                "Title": "example.pdf",
                "Content": "国庆放七天假"
            }
        ],
        "TotalCount": 1,
        "RequestId": "d422c101-96e6-4aeb-b51c-0ccb551a5a52"
    }
}
```

**Example 2: 语义检索（问答对）**

RetrievalSetting.Type参数为QA时，仅检索问答对。

Input: 

```
tccli lkeap RetrieveKnowledge --cli-unfold-argument  \
    --KnowledgeBaseId 49019910106 \
    --Query 国庆节放几天假 \
    --RetrievalMethod SEMANTIC \
    --RetrievalSetting.Type QA
```

Output: 
```
{
    "Response": {
        "Records": [
            {
                "Metadata": {
                    "Type": "QA",
                    "ResultSource": "SEMANTIC"
                },
                "Title": "",
                "Content": "国庆放七天假"
            }
        ],
        "TotalCount": 1,
        "RequestId": "d422c101-96e6-4aeb-b51c-0ccb551a5a52"
    }
}
```

