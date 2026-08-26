**Example 1: 测试**

测试

Input: 

```
tccli monitor DescribeAlarmHistoryShield --cli-unfold-argument  \
    --Module monitor \
    --ShieldPolicyId 2754411
```

Output: 
```
{
    "Response": {
        "CurrentStatus": "EXPIRED",
        "Enable": 1,
        "EndTime": 1728577188,
        "LoopEndDate": 0,
        "LoopStartDate": 0,
        "MetricName": "cpu_usage",
        "MonitorType": "MT_QCE",
        "MonitorTypeShowName": "云产品监控",
        "Name": "",
        "NameSpace": "cvm_device",
        "NameSpaceShowName": "云服务器-基础监控",
        "RequestId": "3e08f0cc-7123-4274-8026-8e7fa147379a",
        "ShieldAlarmLevel": null,
        "ShieldId": "Shield-hbvoj4siyh",
        "ShieldMetric": null,
        "ShieldObject": [
            "{\"appid\":\"251000916\"",
            "\"projectid\":\"0\"",
            "\"vm_uuid\":\"b08d0134-3803-48ce-ba67-5cb38f0dd7d2\"}"
        ],
        "ShieldPolicyId": "2754411",
        "ShieldTag": "ALARMHISTORY",
        "ShieldTimeType": "PERIOD_SHIELD",
        "StartTime": 1728573588,
        "TimeZone": 8
    }
}
```

