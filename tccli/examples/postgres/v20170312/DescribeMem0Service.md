**Example 1: 查询Mem0服务信息**



Input: 

```
tccli postgres DescribeMem0Service --cli-unfold-argument  \
    --DBInstanceId postgres-l0jw845d
```

Output: 
```
{
    "Response": {
        "AgenticBaseId": "agenticbase-2a7vajd1",
        "CreateTime": "2026-07-09 10:48:03",
        "EmbeddingDims": 1024,
        "EmbeddingModel": "kinfra-text-embedding-0.6b",
        "InnerAddress": "",
        "LLMMode": "tokenhub",
        "LLMModel": "auto",
        "NetworkAccessList": [],
        "PGDatabaseName": "mem0",
        "PGUserName": "mem0_user",
        "Status": "creating",
        "UpdateTime": "2026-07-09 10:48:03",
        "RequestId": "a660ca0b-2d26-45d1-9504-4c99522647c3"
    }
}
```

