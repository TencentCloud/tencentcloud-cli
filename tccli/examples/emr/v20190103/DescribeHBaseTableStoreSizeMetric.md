**Example 1: Hbase表维度store size指标监控指标**

获取Hbase表维度store size指标监控指标

Input: 

```
tccli emr DescribeHBaseTableStoreSizeMetric --cli-unfold-argument  \
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
                "MetricDesc": "hbase mem store size",
                "MetricName": "mem_store_size",
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
                    768,
                    768,
                    768,
                    768,
                    768,
                    768,
                    768
                ]
            },
            {
                "MetricDesc": "hbase storefile size",
                "MetricName": "store_file_size",
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
                    10741,
                    10741,
                    10741,
                    10741,
                    10741,
                    10741,
                    10741
                ]
            }
        ],
        "RequestId": "33c3389e-7d67-48d4-bb2f-1728a3201113"
    }
}
```

