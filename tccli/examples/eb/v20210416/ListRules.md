**Example 1: 获取事件规则列表**



Input: 

```
tccli eb ListRules --cli-unfold-argument  \
    --EventBusId eb-l65vlc2
```

Output: 
```
{
    "Response": {
        "RequestId": "bfbf943a-0032-461c-89e6-260f7a3d520d",
        "Rules": [
            {
                "AddTime": "2021-04-29T00:06:22+08:00",
                "Description": "",
                "Enable": true,
                "EventBusId": "eb-l65vlc2u",
                "ModTime": "2021-04-28T16:06:22+08:00",
                "RuleId": "rule-fdltium8",
                "RuleName": "sssss",
                "Status": "Active",
                "Targets": null,
                "DeadLetterConfig": null
            },
            {
                "AddTime": "2021-04-28T16:00:14+08:00",
                "Description": "",
                "Enable": true,
                "EventBusId": "eb-l65vlc2u",
                "ModTime": "2021-04-28T16:00:14+08:00",
                "RuleId": "rule-m5ut05gs",
                "RuleName": "rule",
                "Status": "Active",
                "Targets": null,
                "DeadLetterConfig": null
            }
        ],
        "TotalCount": 2
    }
}
```

