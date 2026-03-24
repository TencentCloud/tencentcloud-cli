**Example 1: 获取账号组列表**

获取账号组列表

Input: 

```
tccli config ListAggregators --cli-unfold-argument  \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "Items": [
            {
                "Name": "账号组1",
                "AccountGroupId": "ca-accountGroupNo1",
                "OwnerUin": 454646534234,
                "AccountCount": 3,
                "Type": "RD",
                "CreateTime": "2023-02-20 10:17:18",
                "Description": "描述"
            }
        ],
        "Total": 1,
        "RequestId": "73d105d8-5820-434f-9fac-76f926e61"
    }
}
```

