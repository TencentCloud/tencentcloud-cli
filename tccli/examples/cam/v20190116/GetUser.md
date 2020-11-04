**Example 1: 查询子用户**



Input: 

```
tccli cam GetUser --cli-unfold-argument  \
    --Name test124
```

Output: 
```
{
    "Response": {
        "Uin": 100000546533,
        "Name": "test124",
        "Uid": 1001774,
        "Remark": "test",
        "ConsoleLogin": 1,
        "PhoneNum": "10086",
        "CountryCode": "86",
        "Email": "123@qq.com",
        "RequestId": "33674182-e53d-416b-b6ce-bd7e7536b5d6"
    }
}
```

