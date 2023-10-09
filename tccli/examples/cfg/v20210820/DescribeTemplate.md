**Example 1: 查询经验**

查询经验

Input: 

```
tccli cfg DescribeTemplate --cli-unfold-argument  \
    --TemplateId 1175
```

Output: 
```
{
    "Response": {
        "RequestId": "e5cf31b7-d530-4bce-8836-4c227b463b31",
        "Template": {
            "AlarmPolicy": [],
            "ApmServiceList": [],
            "Tags": [],
            "TemplateCreateTime": "2023-10-09 11:03:31",
            "TemplateDescription": "测试",
            "TemplateGroups": [
                {
                    "CreateTime": "2023-10-09 11:03:31",
                    "Description": "测试",
                    "Mode": 1,
                    "ObjectTypeId": 1,
                    "Order": 1,
                    "TemplateGroupActions": [
                        {
                            "ActionApiType": 1,
                            "ActionAttribute": 1,
                            "ActionId": 1,
                            "ActionTitle": "关机（测试）",
                            "ActionType": "平台",
                            "CreateTime": "2023-10-09 11:03:31",
                            "CustomConfiguration": "{}",
                            "ExecuteId": null,
                            "GeneralConfiguration": "{\"AliasTitle\": \"\", \"PreTimeWait\": 0, \"ActionTimeout\": 1800, \"AfterTimeWait\": 0}",
                            "Order": 1,
                            "RandomId": 368448,
                            "RecoverId": 232618,
                            "TemplateGroupActionId": 3982,
                            "UpdateTime": "2023-10-09 11:03:31"
                        },
                        {
                            "ActionApiType": 1,
                            "ActionAttribute": 2,
                            "ActionId": 2,
                            "ActionTitle": "开机",
                            "ActionType": "平台",
                            "CreateTime": "2023-10-09 11:03:31",
                            "CustomConfiguration": "{}",
                            "ExecuteId": 368448,
                            "GeneralConfiguration": "{\"PreTimeWait\": 0, \"ActionTimeout\": 1800, \"AfterTimeWait\": 0}",
                            "Order": 2,
                            "RandomId": 232618,
                            "RecoverId": null,
                            "TemplateGroupActionId": 3983,
                            "UpdateTime": "2023-10-09 11:03:31"
                        }
                    ],
                    "TemplateGroupId": 1659,
                    "Title": "测试",
                    "UpdateTime": "2023-10-09 11:03:31"
                }
            ],
            "TemplateId": 1175,
            "TemplateIsUsed": 1,
            "TemplateMode": 1,
            "TemplateMonitors": [
                {
                    "MetricChineseName": "CPU使用率",
                    "MetricId": 614,
                    "MetricName": "CpuUsage",
                    "MonitorId": 2173,
                    "ObjectTypeId": 1
                }
            ],
            "TemplateOwnerUin": "700000174829",
            "TemplatePauseDuration": 60,
            "TemplatePolicy": null,
            "TemplateRegionId": 1,
            "TemplateSource": 0,
            "TemplateTag": "",
            "TemplateTitle": "测试",
            "TemplateUpdateTime": "2023-10-09 11:03:31"
        }
    }
}
```

