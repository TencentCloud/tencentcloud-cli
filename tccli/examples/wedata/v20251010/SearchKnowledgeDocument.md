**Example 1: 检索表知识**



Input: 

```
tccli wedata SearchKnowledgeDocument --cli-unfold-argument  \
    --Queries.0.Fields description \
    --Queries.0.Query 复杂 \
    --Queries.0.SearchMode 1 \
    --WorkspaceId 1 \
    --KbIds 48a8c528-060e-4f96-a797-41c06e5c85bd \
    --KbNames builtin_table
```

Output: 
```
{
    "Response": {
        "Data": {
            "ErrorCode": 0,
            "ErrorMessage": "",
            "Results": [
                {
                    "Document": "{\"catalog\":\"catalogaaaaa\",\"description\":\"这是一个复杂表\",\"metadata\":\"{\\\"a\\\":1}\",\"schema\":\"schemabbbbb\",\"table\":\"tablecccccc\"}",
                    "ExtInfo": "{\"from\": \"wedata\"}",
                    "KbId": "48a8c528-060e-4f96-a797-41c06e5c85bd",
                    "KnId": "catalogaaaaa.schemabbbbb.tablecccccc",
                    "Metadata": "{\"a\":1}",
                    "Score": 0.8776221
                }
            ],
            "Total": 3
        },
        "RequestId": "476a6ded-c887-44b9-9e67-7d7e81ccf384"
    }
}
```

