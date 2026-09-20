**Example 1: 查询指定会话空间详情**

根据会话空间 ID 查询生产客服会话空间的详细信息。

Input: 

```
tccli ags DescribeSessionSpace --cli-unfold-argument  \
    --SpaceId space-198577ac-324e-4e1b-bfda-f75a2365c9df
```

Output: 
```
{
    "Response": {
        "SessionSpace": {
            "CreateTime": "2026-08-17T03:35:11.868Z",
            "Default": false,
            "Description": "Stores sessions for the production customer service application.",
            "Name": "Customer Service Production Space",
            "SpaceId": "space-198577ac-324e-4e1b-bfda-f75a2365c9df",
            "Status": "Active",
            "UpdateTime": "2026-08-17T03:35:11.868Z"
        },
        "RequestId": "7764a908-369a-4bab-8ffb-6446c86b54d6"
    }
}
```

