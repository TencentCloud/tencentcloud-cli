**Example 1: 查询知识库信息**



Input: 

```
tccli vod DescribeKnowledgeBases --cli-unfold-argument  \
    --SubAppId 200000 \
    --Offset 0 \
    --Limit 10 \
    --Name 新的知识库
```

Output: 
```
{
    "Response": {
        "KnowledgeBaseSet": [
            {
                "CreateTime": "2026-06-18T17:08:36+08:00",
                "Description": "这是我刚刚创建的知识库",
                "KnowledgeBaseId": "kb-**********",
                "Name": "新的知识库",
                "Status": "active"
            }
        ],
        "TotalCount": 1,
        "RequestId": "e2ae4af8-928f-4d98-9ef4-faaf7d5bdfdc"
    }
}
```

