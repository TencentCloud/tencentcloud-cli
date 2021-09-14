**Example 1: 获取私有域解析账号列表**



Input: 

```
tccli privatedns DescribePrivateDNSAccountList --cli-unfold-argument  \
    --Limit 200 \
    --Offset 0 \
    --Filters.0.Name AccountUin \
    --Filters.0.Values 123456789
```

Output: 
```
{
    "Response": {
        "RequestId": "14413609-3e4e-9003-c5df01ee3e4b0df7",
        "TotalCount": 1,
        "AccountSet": [
            {
                "Uin": "1234567898",
                "Account": "privatedns***@tencent.com",
                "Nickname": "Private DNS体验账号"
            }
        ]
    }
}
```

