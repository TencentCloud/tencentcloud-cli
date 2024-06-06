**Example 1: 指标订阅预览示例**

指标订阅预览示例

Input: 

```
tccli cls DescribeMetricSubscribePreview --cli-unfold-argument  \
    --Namespace QCE/CVM \
    --Metrics.0.MetricName MemUsed \
    --Metrics.0.Periods 60 \
    --Metrics.0.MetricLabels.0.Key key_demo \
    --Metrics.0.MetricLabels.0.Value value_demo \
    --InstanceInfo.InstanceDimension InstanceId \
    --InstanceInfo.Instances.0.Values ins-izop9bz6
```

Output: 
```
{
    "Response": {
        "FailCount": 0,
        "FailInstances": [],
        "RequestId": "220fa7fb-9134-4dbc-84bb-00613636b45a",
        "SuccessCount": 1,
        "SuccessInstances": [
            {
                "Dimensions": [
                    {
                        "Name": "InstanceId",
                        "Value": "ins-izop9bz6"
                    }
                ],
                "ErrMsg": "",
                "MetricName": "MemUsed",
                "Namespace": "QCE/CVM",
                "Period": 60,
                "CLSMetricName": "qce_cvm_memused_60_avg",
                "Value": 340.166
            }
        ],
        "TotalCount": 1
    }
}
```

