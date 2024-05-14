**Example 1: 查询指标监控数据**



Input: 

```
tccli monitor DescribeDashboardMetricData --cli-unfold-argument  \
    --Query.0.DataSource DS_QCEMetric \
    --Query.0.Namespace QCE/CVM \
    --Query.0.MetricName CpuUsage \
    --Query.0.Aggregate  \
    --Query.0.Period 60 \
    --Query.0.Conditions.0.Region na-toronto \
    --Query.0.Conditions.0.Dimension {"InstanceId":"ins-0o9cty8p"} \
    --Query.0.GroupBy InstanceId \
    --Query.0.StartTime 2020-11-02T15:52:36+08:00 \
    --Query.0.EndTime 2020-11-02T16:52:36+08:00 \
    --Module monitor \
    --SpaceUUID space_default
```

Output: 
```
{
    "Response": {
        "RequestId": "8e0387fa-9871-49ac-a56d-8f080cb9d53e"
    }
}
```

