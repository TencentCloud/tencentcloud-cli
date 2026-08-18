**Example 1: 修改会话空间信息**

调整会话空间名称和描述，使其覆盖订单、退款及售后业务场景。

Input: 

```
tccli ags ModifySessionSpace --cli-unfold-argument  \
    --SpaceId space-75ef3dc0-8523-4e5c-81e3-57ff8a453c7a \
    --Name Order and After-Sales Service Space \
    --Description Stores sessions for order, refund, and after-sales service workflows.
```

Output: 
```
{
    "Response": {
        "SessionSpace": {
            "CreateTime": "2026-08-17T03:50:59.655Z",
            "Default": false,
            "Description": "Stores sessions for order, refund, and after-sales service workflows.",
            "Name": "Order and After-Sales Service Space",
            "SpaceId": "space-75ef3dc0-8523-4e5c-81e3-57ff8a453c7a",
            "Status": "Active",
            "UpdateTime": "2026-08-17T06:08:18.127Z"
        },
        "RequestId": "accebb0a-563d-43a5-ac93-f2f5ce5ae943"
    }
}
```

