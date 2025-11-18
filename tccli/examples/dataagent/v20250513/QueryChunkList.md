**Example 1: 文档切片查询**

文档切片查询

Input: 

```
tccli dataagent QueryChunkList --cli-unfold-argument  \
    --Page 1 \
    --PageSize 50
```

Output: 
```
{
    "Response": {
        "RequestId": "9c8fa705-43d3-4be4-b7fa-5593bd3dd6f4",
        "Total": 1,
        "Chunks": [
            {
                "Id": "f5d1714d-bbba-4e2c-bf48-1378cb5bafe1",
                "Content": "2025-03-21-whitelist",
                "Size": 30
            }
        ]
    }
}
```

