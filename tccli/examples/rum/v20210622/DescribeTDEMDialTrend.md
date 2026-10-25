**Example 1: 查询拨测趋势**

按小时或天返回拨测执行趋势。

Input: 

```
tccli rum DescribeTDEMDialTrend --cli-unfold-argument  \
    --AppId 5 \
    --StartTime 1789026600000 \
    --EndTime 1791618600000 \
    --TaskId 16 \
    --Platform android \
    --AppVersion 1.0.0 \
    --Device sdk_gphone64_arm64 \
    --NetType wifi \
    --Operator 电信 \
    --ClientRegion 广东 \
    --TargetIp 183.2.172.177 \
    --Granularity hour
```

Output: 
```
{
    "Response": {
        "Points": [
            {
                "Time": "2026-09-30 15:00:00",
                "ExecutionCount": 6,
                "SuccessCount": 6,
                "FailCount": 0,
                "AvgDuration": 6.333333333333333
            }
        ],
        "RequestId": "34e659ef-11d5-4dbf-aac5-ec4474c3d633"
    }
}
```

