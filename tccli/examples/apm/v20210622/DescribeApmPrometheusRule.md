**Example 1: test**

查询apm业务系统与Prometheus实例的指标匹配规则

Input: 

```
tccli apm DescribeApmPrometheusRule --cli-unfold-argument  \
    --InstanceId apm-059oXBfTL
```

Output: 
```
{
    "Response": {
        "ApmPrometheusRules": [
            {
                "Id": 1,
                "MetricMatchType": 1,
                "MetricNameRule": "task",
                "Name": "test",
                "ServiceName": "pro",
                "Status": 1
            },
            {
                "Id": 2,
                "MetricMatchType": 0,
                "MetricNameRule": "task.duration",
                "Name": "MyRule",
                "ServiceName": "",
                "Status": 1
            },
            {
                "Id": 3,
                "MetricMatchType": 1,
                "MetricNameRule": "task.duration",
                "Name": "testRule",
                "ServiceName": "",
                "Status": 1
            }
        ],
        "RequestId": "fbacd0d1-d208-435f-a74b-e395213fe420"
    }
}
```

