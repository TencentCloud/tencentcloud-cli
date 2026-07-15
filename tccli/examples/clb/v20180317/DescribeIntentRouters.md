**Example 1: 查询意图路由列表**



Input: 

```
tccli clb DescribeIntentRouters --cli-unfold-argument  \
    --ModelRouterId cmr-abc12345
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "IntentRouterSet": [
            {
                "IntentRouterId": "ir-abc12345",
                "RouteName": "IntentRouter/customer-support",
                "Status": "Active",
                "CreatedTime": "2024-01-01T00:00:00Z",
                "UpdatedTime": "2024-01-01T00:00:00Z"
            }
        ],
        "RequestId": "dde9fece-1d15-4494-ae62-1632cc6b9f6f"
    }
}
```

