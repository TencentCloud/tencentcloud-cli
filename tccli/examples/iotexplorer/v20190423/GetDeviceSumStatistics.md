**Example 1: 拉取设备统计汇总数据示例**



Input: 

```
tccli iotexplorer GetDeviceSumStatistics --cli-unfold-argument  \
    --ProjectId proj-4rf09hhy \
    --ProductIds J2CRPPZ8J4
```

Output: 
```
{
    "Response": {
        "ActivationCount": 1,
        "OnlineCount": 1,
        "ActiveBeforeDay": 20,
        "ActivationBeforeDay": 10,
        "ActivationWeekDayCount": 80,
        "ActiveWeekDayCount": 40,
        "ActivationBeforeWeekDayCount": 100,
        "ActiveBeforeWeekDayCount": 60,
        "RequestId": "6b6e765c-1625-49e6-9743-452e6ce15caa"
    }
}
```

