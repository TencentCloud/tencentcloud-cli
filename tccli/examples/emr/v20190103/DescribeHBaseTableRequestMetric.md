**Example 1: Hbase表维度读写请求指标**

获取Hbase表维度读写请求指标

Input: 

```
tccli emr DescribeHBaseTableRequestMetric --cli-unfold-argument  \
    --InstanceId emr-lvr4kbpk \
    --TableName hbase_meta \
    --StartTime 1764826199 \
    --EndTime 1764828199
```

Output: 
```
{
    "Response": {
        "MetricDataList": [
            {
                "MetricDesc": "read request rate",
                "MetricName": "read_request_rate",
                "Timestamps": [
                    1764826200,
                    1764826500,
                    1764826800,
                    1764827100,
                    1764827400,
                    1764827700,
                    1764828000
                ],
                "Values": [
                    0.01,
                    0.01,
                    0.01,
                    0.01,
                    0.01,
                    0.01,
                    0.01
                ]
            },
            {
                "MetricDesc": "write request rate",
                "MetricName": "write_request_rate",
                "Timestamps": [
                    1764826200,
                    1764826500,
                    1764826800,
                    1764827100,
                    1764827400,
                    1764827700,
                    1764828000
                ],
                "Values": [
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0
                ]
            }
        ],
        "RequestId": "fa272328-a8f8-4b00-ae01-d627d6c597d1"
    }
}
```

