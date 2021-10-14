**Example 1: 获取已验证的手机邮箱列表**



Input: 

```
tccli domain DescribePhoneEmailList --cli-unfold-argument  \
    --Type 1 \
    --Offset 0 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "PhoneEmailList": [
            {
                "Code": "12376542345",
                "Type": 1,
                "CreatedOn": "2021-09-12 12:12:34"
            }
        ],
        "TotalCount": 1,
        "RequestId": "xx"
    }
}
```

