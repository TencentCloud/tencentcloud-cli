**Example 1: 获取增值服务列表**

获取增值服务列表

Input: 

```
tccli dnspod DescribeVasList --cli-unfold-argument  \
    --Offset 0 \
    --Limit 10 \
    --DomainId 12
```

Output: 
```
{
    "Response": {
        "RequestId": "27c8df50-206e-42db-a031-8b7f15c0d2dc",
        "VasList": [
            {
                "LimitNumber": 5,
                "StartedAt": "2022-05-22",
                "EndedAt": "2023-05-22",
                "ResourceId": "9axxxc77",
                "AutoRenew": "default",
                "Domain": "example.com",
                "BindType": "user",
                "Key": "ptr",
                "Name": "PTR 反解析记录",
                "CanRenew": true,
                "VipDomain": false
            }
        ],
        "TotalCount": 1
    }
}
```

