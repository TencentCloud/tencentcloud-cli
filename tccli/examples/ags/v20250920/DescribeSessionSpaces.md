**Example 1: 分页查询会话空间**

查询当前应用及地域下的会话空间列表，每页返回 20 条数据。

Input: 

```
tccli ags DescribeSessionSpaces --cli-unfold-argument  \
    --Offset 0 \
    --Limit 20
```

Output: 
```
{
    "Response": {
        "SessionSpaces": [
            {
                "CreateTime": "2026-08-17T03:51:17.608Z",
                "Default": false,
                "Description": "Reserved for sessions generated during a seasonal marketing campaign.",
                "Name": "Seasonal Campaign Temporary Space",
                "SpaceId": "space-22eed49f-e3ae-4b4a-8efa-4cd961bf4764",
                "Status": "Active",
                "UpdateTime": "2026-08-17T03:51:17.608Z"
            }
        ],
        "TotalCount": 3,
        "RequestId": "9d08f066-c47e-4e5d-ae9c-a51d7edf01a6"
    }
}
```

