**Example 1: 获取账户信息**

获取账户信息

Input: 

```
tccli dnspod DescribeUserDetail --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "ab4f1426-ea15-42ea-8183-dc1b44151166",
        "UserInfo": {
            "Nick": "jionly",
            "Id": 5299600,
            "Email": "qcloud_uin_100000000328@qcloud.com",
            "Status": "enabled",
            "Telephone": "187****3214",
            "EmailVerified": "yes",
            "TelephoneVerified": "yes",
            "UserGrade": "DP_Free",
            "RealName": "王小云",
            "WechatBinded": "no",
            "Uin": 100000000328,
            "FreeNs": [
                "hannah.dnspod.net",
                "perch.dnspod.net"
            ]
        }
    }
}
```

