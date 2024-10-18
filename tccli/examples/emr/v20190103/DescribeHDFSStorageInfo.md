**Example 1: DescribeHDFSStorageInfo**



Input: 

```
tccli emr DescribeHDFSStorageInfo --cli-unfold-argument  \
    --InstanceId abc \
    --StartTime 0 \
    --EndTime 0
```

Output: 
```
{
    "Response": {
        "SampleTime": 0,
        "StorageSummaryDistribution": [
            {
                "MetricItem": "abc",
                "MetricName": "abc",
                "Dps": [
                    {
                        "Timestamp": "abc",
                        "Value": "abc"
                    }
                ]
            }
        ],
        "RequestId": "abc"
    }
}
```

