**Example 1: 获取已验证的手机邮箱列表**



Input: 

```
tccli domain DescribeIntlPhoneEmailList --cli-unfold-argument  \
    --Type 2 \
    --Limit 30 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "PhoneEmailList": [
            {
                "Code": "1234567@test.com",
                "Type": 2,
                "CreatedOn": "2021-11-10 14:42:12"
            }
        ],
        "TotalCount": 1,
        "RequestId": "eac6b301-a322-493a-8e36-83b295459398"
    }
}
```

