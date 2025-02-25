**Example 1: 查询环境下的知识库列表**

查询环境下的知识库列表

Input: 

```
tccli lowcode DescribeKnowledgeSetList --cli-unfold-argument  \
    --EnvId lowcode-xxxx \
    --Offset 0 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "Data": {
            "KnowledgeSets": [
                {
                    "Name": "test",
                    "Title": "testTiTle",
                    "Desc": "test",
                    "Active": "ENABLED",
                    "CreateTime": "2024-06-04 18:07:38",
                    "UpdateTime": "2024-06-04 18:09:29"
                }
            ],
            "Total": 1
        },
        "RequestId": "f549082e-0cff-4026-96f6-a570d9f1c22d"
    }
}
```

