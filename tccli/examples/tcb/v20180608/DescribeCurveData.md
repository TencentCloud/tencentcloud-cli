**Example 1: 根据用户传入的指标以及时间粒度，拉取一段时间内的监控数据**

静态托管相关指标，无须传入ResourceID。传入与时间范围相匹配的时间粒度Period，返回指定时间粒度和时间范围的监控数据。

Input: 

```
tccli tcb DescribeCurveData --cli-unfold-argument  \
    --EnvId envid-xxxxx \
    --MetricName StaticFsSizePkg \
    --StartTime 2026-02-05 00:00:00 \
    --EndTime 2026-02-06 23:59:59 \
    --Period 3600
```

Output: 
```
{
    "Response": {
        "EndTime": "2026-02-06 23:00:00",
        "MetricName": "StaticFsSizePkg",
        "NewValues": [
            1
        ],
        "Period": 3600,
        "StartTime": "2026-02-05 00:00:00",
        "Statistics": "last",
        "Time": [
            1770220800
        ],
        "Values": [
            1
        ],
        "RequestId": "74126bc4-9fa1-4891-891b-b9ba41ea664a"
    }
}
```

**Example 2: 根据用户传入的指标以及资源id，拉取一段时间内的监控数据**

查询云托管某个版本的监控数据，需要传入ResourceID以及SubresourceID。不传入period，返回默认时间粒度的指标。

Input: 

```
tccli tcb DescribeCurveData --cli-unfold-argument  \
    --EnvId envid-xxxxx \
    --MetricName TkeHttpErrorService \
    --StartTime 2026-03-13 00:00:00 \
    --EndTime 2026-03-16 23:59:59 \
    --ResourceID ibot-agent123 \
    --SubresourceID ibot-agent123-001
```

Output: 
```
{
    "Response": {
        "EndTime": "2026-03-16 23:00:00",
        "MetricName": "TkeHttpErrorService",
        "NewValues": [
            0
        ],
        "Period": 3600,
        "StartTime": "2026-03-13 00:00:00",
        "Statistics": "sum",
        "Time": [
            1773331200
        ],
        "Values": [
            0
        ],
        "RequestId": "e9271644-4eb0-4b17-981a-330f2ca534b1"
    }
}
```

**Example 3: 根据用户传入的指标，拉取一段时间内的监控数据**

云托管相关指标，需要传入ResourceID。不传入period，返回默认时间粒度的指标。

Input: 

```
tccli tcb DescribeCurveData --cli-unfold-argument  \
    --EnvId envid-xxxxxxx \
    --MetricName TkeInvokeNumService \
    --StartTime 2026-03-16 00:00:00 \
    --EndTime 2026-03-16 23:59:59 \
    --ResourceID ibot-agent123
```

Output: 
```
{
    "Response": {
        "EndTime": "2026-03-16 23:55:00",
        "MetricName": "TkeInvokeNumService",
        "NewValues": [
            0
        ],
        "Period": 300,
        "StartTime": "2026-03-16 00:00:00",
        "Statistics": "sum",
        "Time": [
            1773590400
        ],
        "Values": [
            0
        ],
        "RequestId": "cd2cec9d-c0e9-4bab-b889-0ccc230cdc83"
    }
}
```

