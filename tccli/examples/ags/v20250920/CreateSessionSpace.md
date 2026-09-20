**Example 1: 创建生产环境会话空间**

为生产环境的客服应用创建独立会话空间，用于隔离会话、事件和用户状态数据。

Input: 

```
tccli ags CreateSessionSpace --cli-unfold-argument  \
    --Name Customer Service Production Space \
    --Description Stores sessions for the production customer service application.
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
        "RequestId": "5bf9b472-8e6d-453f-ab2f-f2b7c332fc5c"
    }
}
```

