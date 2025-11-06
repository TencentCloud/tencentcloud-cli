**Example 1: 获取账户信息**

获取账户信息

Input: 

```
tccli dnspod DescribeUserDetail --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "8b7a2ed1-0f04-4cf6-b5b1-b77f91572f34",
        "UserInfo": {
            "AllowTransferIn": false,
            "Email": "qcloud_uin_123456@qcloud.com",
            "EmailVerified": "yes",
            "FreeNs": [
                "v4u4f.dnspod.net",
                "c6b8q.dnspod.net"
            ],
            "Id": 123456,
            "Nick": "",
            "RealName": "",
            "Status": "enabled",
            "Telephone": "",
            "TelephoneVerified": "yes",
            "Uin": 123456,
            "UserGrade": "DP_Free",
            "WechatBinded": "no"
        }
    }
}
```

