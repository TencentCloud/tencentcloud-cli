**Example 1: 查询策略组信息**



Input: 

```
tccli monitor DescribePolicyGroupInfo --cli-unfold-argument  \
    --Module monitor \
    --GroupId 11111
```

Output: 
```
{
    "Response": {
        "Callback": null,
        "CanSetDefault": true,
        "ConditionsConfig": [
            {
                "AlarmNotifyPeriod": 86400,
                "AlarmNotifyType": 0,
                "CalcType": 1,
                "CalcValue": "0",
                "ContinueTime": 60,
                "MetricId": 33,
                "MetricShowName": "CPU利用率",
                "Period": 60,
                "RuleId": 200000,
                "Unit": "%"
            }
        ],
        "ConditionsTemp": null,
        "DimensionGroup": [
            "unInstanceId"
        ],
        "EventConfig": [
            {
                "AlarmNotifyPeriod": 86400,
                "AlarmNotifyType": 0,
                "EventId": 42,
                "EventShowName": "ping不可达",
                "RuleId": 200001
            }
        ],
        "GroupName": "策略组名称test",
        "IsDefault": 0,
        "LastEditUin": "1500000000",
        "ProjectId": 0,
        "ReceiverInfos": null,
        "Region": [
            "bj",
            "ca",
            "cd",
            "de",
            "gz",
            "gzopen",
            "hk",
            "hzec",
            "jnec",
            "jp",
            "kr",
            "nj",
            "sg",
            "sh",
            "shjr",
            "tsn",
            "usw"
        ],
        "Remark": "",
        "RequestId": "11111111-1111-1111-1111-111111111111",
        "ShowName": "云服务器-基础监控",
        "UpdateTime": "2018-07-09 15:56:55",
        "ViewName": "cvm_device"
    }
}
```

