**Example 1: 获取已验证的手机邮箱列表**

默认

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
                "Code": "abc",
                "Type": 1,
                "CreatedOn": "abc",
                "CheckStatus": 0
            }
        ],
        "TotalCount": 1,
        "RequestId": "abc"
    }
}
```

