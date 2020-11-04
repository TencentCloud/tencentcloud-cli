**Example 1: 查看权限规则列表**

查看权限规则列表

Input: 

```
tccli chdfs DescribeAccessRules --cli-unfold-argument  \
    --AccessGroupId ag-jwmfdcul
```

Output: 
```
{
    "Response": {
        "AccessRules": [
            {
                "AccessRuleId": 13001,
                "Address": "127.0.0.1",
                "AccessMode": 1,
                "Priority": 1,
                "CreateTime": "2019-07-30T16:24:38+08:00"
            },
            {
                "AccessRuleId": 13002,
                "Address": "127.0.0.1",
                "AccessMode": 2,
                "Priority": 2,
                "CreateTime": "2019-07-30T16:24:38+08:00"
            }
        ],
        "RequestId": "19d240f4-156d-4a3c-856c-216d64a6bb4a"
    }
}
```

