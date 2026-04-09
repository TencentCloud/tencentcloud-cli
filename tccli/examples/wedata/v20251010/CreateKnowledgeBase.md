**Example 1: 测试**



Input: 

```
tccli wedata CreateKnowledgeBase --cli-unfold-argument  \
    --Fields.0.EnableEmbedding True \
    --Fields.0.EnableKeyword True \
    --Fields.0.Name key \
    --Fields.0.Type text \
    --Name qizhi1231111111111111 \
    --WorkspaceId 1 \
    --Description 这是一个描述 \
    --EmbeddingDim 2048 \
    --Tags test1
```

Output: 
```
{
    "Response": {
        "Data": {
            "ErrorCode": 0,
            "ErrorMessage": "",
            "KbId": "a62bf901-8cbf-44a5-96a0-e836f589c7f3"
        },
        "RequestId": "0e258a29-89ea-4b22-9d17-28803a34ef8a"
    }
}
```

