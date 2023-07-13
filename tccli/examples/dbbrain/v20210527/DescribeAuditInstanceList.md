**Example 1: 查询实例列表**

查询需要开通审计的实例列表。

Input: 

```
tccli dbbrain DescribeAuditInstanceList --cli-unfold-argument  \
    --Product dcdb \
    --NodeRequestType dcdb \
    --AuditSwitch 0 \
    --Offset 0 \
    --Limit 50
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "RequestId": "b39db780-0b49-11ee-8525-17d65d16bdaf",
        "Items": [
            {
                "BillingConfirmed": 1,
                "AuditStatus": "ON",
                "ColdLogExpireDay": 23,
                "InstanceId": "tdsql-lq5ue8p7",
                "LogExpireDay": 30,
                "CreateTime": "2023-06-08 19:48:19",
                "HotLogSize": 0,
                "HotLogExpireDay": 7,
                "BillingAmount": 0,
                "ColdLogSize": 0,
                "InstanceInfo": {
                    "InstanceName": "DBbrain测试_fanzhi_MySQL8.0",
                    "AuditStatus": 1,
                    "AppId": 251009273,
                    "InstanceId": "tdsql-lq5ue8p7",
                    "ResourceTags": [
                        "abc"
                    ],
                    "ProjectId": 0,
                    "Region": "ap-guangzhou"
                }
            }
        ]
    }
}
```

