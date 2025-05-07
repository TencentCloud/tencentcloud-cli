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
                "Code": "137***3434",
                "Type": 1,
                "CreatedOn": "2023-03-10 10:00:00",
                "CheckStatus": 1
            }
        ],
        "TotalCount": 1,
        "RequestId": "f376d0e6-f064-1234-b27f-a8ae3b054dfa"
    }
}
```

