**Example 1: 列出实例下所有告警规则**

列出实例下所有告警规则，包含启用与禁用

Input: 

```
tccli monitor DescribePrometheusAlertGroups --cli-unfold-argument  \
    --InstanceId prom-xxxxxxxx
```

Output: 
```
{
    "Response": {
        "AlertGroupSet": [
            {
                "AMPReceivers": [],
                "CreatedAt": "2023-08-01T20:29:56+08:00",
                "CustomReceiver": {
                    "Type": "",
                    "Url": ""
                },
                "GroupId": "alert-xxxxxxxx",
                "GroupName": "查询告警分组测试-1",
                "Rules": [
                    {
                        "Annotations": [
                            {
                                "Key": "summary",
                                "Value": "{{$value}}"
                            }
                        ],
                        "Duration": "",
                        "Expr": "expr1",
                        "Labels": [
                            {
                                "Key": "_interval_",
                                "Value": "10m"
                            }
                        ],
                        "RuleName": "规则-1",
                        "State": 2
                    }
                ],
                "TemplateId": "",
                "UpdatedAt": "2023-08-01T20:29:56+08:00"
            }
        ],
        "RequestId": "bc70036f-db50-4b46-abbc-bd41eeb06f7a",
        "TotalCount": 1
    }
}
```

