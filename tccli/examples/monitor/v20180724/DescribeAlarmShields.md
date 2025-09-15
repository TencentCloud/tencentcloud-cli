**Example 1: 检索**



Input: 

```
tccli monitor DescribeAlarmShields --cli-unfold-argument  \
    --Module monitor \
    --PageNumber 1 \
    --PageSize 2 \
    --Order DESC \
    --Field updated_at
```

Output: 
```
{
    "Response": {
        "RequestId": "a44499af-3cab-4b08-8929-7e9a935d3640",
        "Shields": [
            {
                "CurrentStatus": "TRIGGERING",
                "Description": "",
                "Enable": 1,
                "EndTime": 0,
                "LoopEndDate": 0,
                "LoopStartDate": 0,
                "MonitorType": "MT_QCE",
                "MonitorTypeShowName": "云产品监控",
                "Name": "Eric测试告警历史标记",
                "NameSpace": "cvm_device",
                "NameSpaceShowName": "云服务器-基础监控",
                "ShieldAlarmLevel": null,
                "ShieldEvent": null,
                "ShieldEventFlag": 1,
                "ShieldId": "Shield-al7vv5ctsw",
                "ShieldMetric": null,
                "ShieldMetricFlag": 1,
                "ShieldObject": [
                    ""
                ],
                "ShieldPolicyId": "policy-ebsymnax",
                "ShieldPolicyName": "Eric-新增收敛测试-5",
                "ShieldTimeType": "FOREVER_SHIELD",
                "StartTime": 0,
                "TimeZone": 8,
                "VersionTag": "POLICY"
            }
        ],
        "TotalCount": 50
    }
}
```

