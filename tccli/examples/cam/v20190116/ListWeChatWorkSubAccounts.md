**Example 1: 拉取企业微信子用户**



Input: 

```
tccli cam ListWeChatWorkSubAccounts --cli-unfold-argument  \
    --Offset 0 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "TotalCount": 100,
        "Data": [
            {
                "Uin": 100000546533,
                "Name": "test124",
                "Uid": 1001774,
                "Remark": "test",
                "ConsoleLogin": 1,
                "PhoneNum": "10086",
                "CountryCode": "86",
                "Email": "123@qq.com",
                "WeChatWorkUserId": "xxx",
                "CreateTime": "2020-10-10 00:00:00"
            }
        ],
        "RequestId": "33674182-e53d-416b-b6ce-bd7e7536b5d6"
    }
}
```

