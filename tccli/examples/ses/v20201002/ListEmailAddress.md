**Example 1: 获取发信地址列表**



Input: 

```
tccli ses ListEmailAddress --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "8979fc1e-9564-4fc9-bf7d-2958ce679b72",
        "EmailSenders": [
            {
                "EmailAddress": "service@mail.qcloud.com",
                "EmailSenderName": "腾讯云邮件通知",
                "CreatedTimestamp": 1602143617
            },
            {
                "EmailAddress": "verify@mail.qcloud.com",
                "EmailSenderName": "腾讯云验证码",
                "CreatedTimestamp": 1602143617
            }
        ]
    }
}
```

