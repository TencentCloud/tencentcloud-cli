**Example 1: 示例 一**

获取日志详情示例

Input: 

```
tccli wedata GetInstanceLog --cli-unfold-argument  \
    --ProjectId 1460947878944567296 \
    --InstanceKey 20250326150742906_2025-03-28 00:00:00 \
    --LifeRoundNum 0 \
    --ScheduleTimeZone UTC+6 \
    --BrokerIp ins-6m365yvb \
    --ExecutionJobId 6820250328000318055 \
    --LogLevel All \
    --StartLineNum 1 \
    --EndLineCount 10000
```

Output: 
```
{
    "Response": {
        "Data": {
            "BrokerIp": "ins-6m365yvb",
            "CodeFileSize": "1 KB",
            "CodeInfo": "echo this is log demo;",
            "EndTime": "2025-03-27 22:18:59",
            "ExtInfo": "45308",
            "InstanceKey": "20250326150742906_2025-03-28 00:00:00",
            "InstanceState": 2,
            "IsEnd": true,
            "LineCount": 331,
            "LogFileSize": "1 KB",
            "LogInfo": "2025-03-28 00:18:37 this is log demo",
            "ProjectId": "1460947878944567296",
            "RunType": "PERIODIC",
            "StartTime": "2025-03-27 22:18:43"
        },
        "RequestId": "724045bb-9cad-44ff-8311-bf5c79f7bff0"
    }
}
```

