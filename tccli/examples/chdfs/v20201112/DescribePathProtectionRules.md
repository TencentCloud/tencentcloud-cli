**Example 1: 查看路径保护规则列表**

查看路径保护规则列表

Input: 

```
tccli chdfs DescribePathProtectionRules --cli-unfold-argument  \
    --FileSystemId f4mnvilzmdd
```

Output: 
```
{
    "Response": {
        "PathProtectionRules": [
            {
                "PathProtectionRuleId": 1,
                "Name": "test",
                "Path": "/protect1",
                "Status": 1,
                "CreateTime": "2019-07-30T16:24:38+08:00"
            },
            {
                "PathProtectionRuleId": 2,
                "Name": "test",
                "Path": "/protect2",
                "Status": 1,
                "CreateTime": "2019-07-30T16:24:38+08:00"
            }
        ],
        "RequestId": "19d240f4-156d-4a3c-856c-216d64a6bb4a"
    }
}
```

