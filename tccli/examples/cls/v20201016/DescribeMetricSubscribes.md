**Example 1: 获取指标订阅配置信息**

获取指标订阅配置信息

Input: 

```
tccli cls DescribeMetricSubscribes --cli-unfold-argument  \
    --TopicId 715094e3-01b0-4aeb-91f5-ee9f46a4a13c \
    --Filters.0.Key name \
    --Filters.0.Values template_1 \
    --Offset 0 \
    --Limit 1
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "Datas": [
            {
                "TopicId": "715094e3-01b0-4aeb-91f5-ee9f46a4a13c",
                "TaskId": "5871c48d-219b-4274-829b-5aa7fb24229b",
                "Name": "metric_subscribe_name",
                "Namespace": "QCE/CVM",
                "Metrics": [
                    {
                        "MetricName": "metric name",
                        "Periods": [
                            60,
                            120
                        ],
                        "MetricLabels": [
                            {
                                "Key": "label_key",
                                "Value": "label_value"
                            }
                        ]
                    }
                ],
                "InstanceInfo": {
                    "InstanceDimension": [
                        "bucket",
                        "appid"
                    ],
                    "Instances": [
                        {
                            "Values": [
                                "bucket_asdfa-asdf-asdf-ads",
                                "12325435"
                            ]
                        }
                    ]
                },
                "Enable": 2,
                "Status": 1,
                "ErrMsg": "",
                "CreateTime": 1700200000,
                "UpdateTime": 1700200000
            }
        ],
        "RequestId": "1111c48d-219b-4274-829b-5aa7fb24229b"
    }
}
```

