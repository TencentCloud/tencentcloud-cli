**Example 1: 查询边缘函数副本列表**

查询站点 ID 为 zone-3exa7oergn0l 下的边缘函数 ID 为 ef-crkwnfy0 的边缘函数副本列表。

Input: 

```
tccli teo DescribeFunctionReplicas --cli-unfold-argument  \
    --ZoneId zone-3exa7oergn0l \
    --FunctionId ef-crkwnfy0 \
    --Offset 0 \
    --Limit 10 \
    --SortBy created-on \
    --SortOrder desc
```

Output: 
```
{
    "Response": {
        "FunctionReplicas": [
            {
                "Content": "addEventListener('fetch', e => {\r\n  const response = new Response('Hello World 2!');\r\n  e.respondWith(response);\r\n});",
                "CreatedOn": "2026-01-19T10:22:55+08:00",
                "FunctionId": "ef-crkwnfy0",
                "ModifiedOn": "2026-01-19T11:48:52+08:00",
                "Remark": "Hello World Replica",
                "ReplicaName": "Hello-World-Replica"
            }
        ],
        "TotalCount": 1,
        "RequestId": "9fc970ff-64bf-4234-a010-a8a7875f77f7"
    }
}
```

