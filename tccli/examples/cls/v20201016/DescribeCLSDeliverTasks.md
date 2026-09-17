**Example 1: 查询跨账号投递任务列表**



Input: 

```
tccli cls DescribeCLSDeliverTasks --cli-unfold-argument  \
    --Offset 0 \
    --Limit 1
```

Output: 
```
{
    "Response": {
        "Infos": [
            {
                "Compliance": 1,
                "CreateTime": 1776754097,
                "DeliverRule": {
                    "DataScope": 3
                },
                "Enable": 0,
                "HasServicesLog": 2,
                "Progress": 0,
                "SourceTopicConfig": {
                    "LogsetId": "e83e2d17-6d97-429d-b073-acbcd625ad5f",
                    "TopicFilterType": 1,
                    "Topics": [
                        {
                            "TopicId": "871710c5-35cd-4d1e-8e79-2fa92c35d612"
                        }
                    ]
                },
                "Status": 0,
                "TargetTopicConfig": {
                    "AccountType": 1,
                    "LogsetId": "b*******-diy-1254139626",
                    "Region": "ap-**************",
                    "TopicId": "12cd155d-feb0-497e-929d-dd0070867599"
                },
                "TaskId": "075210cd-28ac-497c-8575-8e0e5e11e1db",
                "TaskName": "update",
                "Uin": 100001127589,
                "UpdateTime": 1776915747
            }
        ],
        "Total": 7,
        "RequestId": "42c19473-518f-4f2e-810f-a3329cdc6709"
    }
}
```

