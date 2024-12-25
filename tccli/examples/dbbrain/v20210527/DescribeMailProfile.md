**Example 1: 获取邮件配置**



Input: 

```
tccli dbbrain DescribeMailProfile --cli-unfold-argument  \
    --Product mysql \
    --ProfileType scheduler_mail_configuration \
    --Offset 0 \
    --Limit 20
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "RequestId": "c7324330-5fc8-11eb-a3f4-96666666",
        "ProfileList": [
            {
                "ProfileId": "1433288",
                "ProfileType": "dbScan_mail_configuration",
                "ProfileLevel": "User",
                "ProfileName": "测试uin",
                "ProfileInfo": {
                    "MailConfiguration": {
                        "HealthStatus": [
                            "HEALTH",
                            "SUB_HEALTH",
                            "RISK",
                            "HIGH_RISK"
                        ],
                        "Region": [
                            "ap-guangzhou"
                        ],
                        "ContactGroup": [],
                        "SendMail": 0,
                        "ContactPerson": [
                            24332
                        ]
                    },
                    "Language": "zh"
                }
            }
        ]
    }
}
```

