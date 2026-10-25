**Example 1: 查询拨测概览**

按时间窗汇总执行次数、成功次数、失败次数、平均时延和丢包率。

Input: 

```
tccli rum DescribeTDEMDialOverview --cli-unfold-argument  \
    --AppId 5 \
    --StartTime 1790092800000 \
    --EndTime 1790784000000 \
    --TaskId 1 \
    --Platform android \
    --AppVersion 1.0.0 \
    --Device sdk_gphone64_arm64 \
    --NetType wifi \
    --Operator 电信 \
    --ClientRegion 广东 \
    --TargetIp 183.2.172.177
```

Output: 
```
{
    "Response": {
        "AvgDuration": 0,
        "AvgLoss": 0,
        "ExecutionCount": 0,
        "FailCount": 0,
        "SuccessCount": 0,
        "TaskCount": 0,
        "RequestId": "2928f594-d8fc-49cd-a80f-e424320bba15"
    }
}
```

