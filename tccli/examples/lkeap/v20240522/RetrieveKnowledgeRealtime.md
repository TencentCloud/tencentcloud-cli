**Example 1: 实时语义检索**

实时语义检索

Input: 

```
tccli lkeap RetrieveKnowledgeRealtime --cli-unfold-argument  \
    --KnowledgeBaseId 49019910106 \
    --Query 国庆节放几天假 \
    --DocIds 1828720159590123264 \
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

