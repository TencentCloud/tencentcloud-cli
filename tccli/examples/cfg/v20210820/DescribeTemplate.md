**Example 1: 查询经验库详情**



Input: 

```
tccli cfg DescribeTemplate --cli-unfold-argument  \
    --TemplateId 509
```

Output: 
```
{
    "Response": {
        "RequestId": "f5a67ce9-74a4-4825-9e0b-e9c13ef12463",
        "Template": {
            "Tags": [
                {
                    "TagKey": "xx",
                    "TagValue": "xxxxx"
                }
            ],
            "TemplateId": 509,
            "TemplateTitle": "test",
            "TemplateDescription": "test",
            "TemplateTag": "test",
            "TemplateIsUsed": 2,
            "TemplateCreateTime": "2021-09-28 15:38:00",
            "TemplateUpdateTime": "2021-10-11 16:26:45",
            "TemplateMode": 1,
            "TemplateRegionId": 1,
            "TemplatePauseDuration": 1,
            "TemplateOwnerUin": "600000559519",
            "TemplateGroups": [
                {
                    "TemplateGroupId": 439,
                    "TemplateGroupActions": [
                        {
                            "TemplateGroupActionId": 865,
                            "ActionId": 1,
                            "ActionTitle": "关机",
                            "ActionApiType": 1,
                            "ActionAttribute": 1,
                            "Order": 1,
                            "GeneralConfiguration": "{}",
                            "CustomConfiguration": "{}",
                            "RandomId": null,
                            "RecoverId": null,
                            "ExecuteId": null,
                            "CreateTime": "2021-09-28 15:38:00",
                            "UpdateTime": "2021-09-28 15:38:00"
                        }
                    ],
                    "Title": "test",
                    "Description": "test",
                    "Order": 1,
                    "Mode": 1,
                    "ObjectTypeId": 1,
                    "CreateTime": "2021-09-28 15:38:00",
                    "UpdateTime": "2021-09-28 15:38:00"
                }
            ],
            "TemplateMonitors": [
                {
                    "MonitorId": 772,
                    "ObjectTypeId": 1,
                    "MetricName": "test",
                    "MetricChineseName": "test"
                },
                {
                    "MonitorId": 773,
                    "ObjectTypeId": 3,
                    "MetricName": "字符串",
                    "MetricChineseName": "字符串"
                }
            ],
            "TemplatePolicy": {
                "TemplatePolicyIdList": [
                    "test"
                ],
                "TemplatePolicyRule": "test",
                "TemplatePolicyDealType": 1
            }
        }
    }
}
```

