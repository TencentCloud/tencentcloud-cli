**Example 1: 示例**

根据用户传入的指标, 拉取一段时间内的监控数据

Input: 

```
tccli tcb DescribeCurveData --cli-unfold-argument  \
    --MetricName StorageRead \
    --StartTime 2019-04-0209:00:00 \
    --EndTime 2019-04-0419:00:00 \
    --ResourceID 3 \
    --EnvId lotestapi100004
```

Output: 
```
{
    "Response": {
        "EndTime": "2019-04-04 19:00:00",
        "MetricName": "StorageRead",
        "Period": 3600,
        "RequestId": "6702e6bd-858d-4b19-89bb-5b183540186d",
        "StartTime": "2019-04-02 09:00:00",
        "Time": [
            1554894000,
            1554894300,
            1554894600,
            1554894900,
            1554895200
        ],
        "Values": [
            20,
            100,
            180,
            240,
            260
        ],
        "NewValues": [
            20,
            100,
            180,
            240,
            260
        ]
    }
}
```

