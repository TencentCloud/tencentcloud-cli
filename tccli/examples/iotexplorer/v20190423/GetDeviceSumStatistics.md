**Example 1: 拉取设备统计汇总数据示例**



Input: 

```
tccli iotexplorer GetDeviceSumStatistics --cli-unfold-argument  \
    --ProjectId prj-zunfat46 \
    --ProductIds [4GDIU5HTEN]
```

Output: 
```
{
    "Response": {
        "ActivationBeforeWeekDayCount": 100,
        "ActiveBeforeWeekDayCount": 60,
        "RequestId": "6b6e765c-1625-49e6-9743-452e6ce15caa"
    }
}
```

