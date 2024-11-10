**Example 1: DescribeHDFSStorageInfo**



Input: 

```
tccli emr DescribeHDFSStorageInfo --cli-unfold-argument  \
    --InstanceId emr-123 \
    --StartTime 1729746447 \
    --EndTime 1729746447
```

Output: 
```
{
    "Response": {
        "RequestId": "040d2297-a88c-4b68-acd4-a48be8699270",
        "SampleTime": 1729738900,
        "StorageSummaryDistribution": [
            {
                "Dps": [
                    {
                        "Timestamp": "1729738900",
                        "Value": "177"
                    }
                ],
                "MetricItem": "empty_count",
                "MetricName": "空文件"
            },
            {
                "Dps": [
                    {
                        "Timestamp": "1729738900",
                        "Value": "1471"
                    }
                ],
                "MetricItem": "hot_count",
                "MetricName": "热文件"
            },
            {
                "Dps": [
                    {
                        "Timestamp": "1729738900",
                        "Value": "133"
                    }
                ],
                "MetricItem": "other_atime_count",
                "MetricName": "其他"
            },
            {
                "Dps": [
                    {
                        "Timestamp": "1729738900",
                        "Value": "14405757446"
                    }
                ],
                "MetricItem": "other_file_size",
                "MetricName": "其他"
            },
            {
                "Dps": [
                    {
                        "Timestamp": "1729738900",
                        "Value": "1669"
                    }
                ],
                "MetricItem": "warm_count",
                "MetricName": "温文件"
            },
            {
                "Dps": [
                    {
                        "Timestamp": "1729738900",
                        "Value": "2767"
                    }
                ],
                "MetricItem": "small_count",
                "MetricName": "小文件"
            },
            {
                "Dps": [
                    {
                        "Timestamp": "1729738900",
                        "Value": "485404741"
                    }
                ],
                "MetricItem": "small_file_size",
                "MetricName": "小文件"
            },
            {
                "Dps": [
                    {
                        "Timestamp": "1729738900",
                        "Value": "14891162187"
                    }
                ],
                "MetricItem": "total_size",
                "MetricName": "总量"
            },
            {
                "Dps": [
                    {
                        "Timestamp": "1729738900",
                        "Value": "5474041684"
                    }
                ],
                "MetricItem": "warm_size",
                "MetricName": "温文件"
            },
            {
                "Dps": [
                    {
                        "Timestamp": "1729738900",
                        "Value": "0"
                    }
                ],
                "MetricItem": "big_count",
                "MetricName": "大文件"
            },
            {
                "Dps": [
                    {
                        "Timestamp": "1729738900",
                        "Value": "0"
                    }
                ],
                "MetricItem": "big_file_size",
                "MetricName": "大文件"
            },
            {
                "Dps": [
                    {
                        "Timestamp": "1729738900",
                        "Value": "0"
                    }
                ],
                "MetricItem": "cold_size",
                "MetricName": "冷文件"
            },
            {
                "Dps": [
                    {
                        "Timestamp": "1729738900",
                        "Value": "2206625015"
                    }
                ],
                "MetricItem": "other_atime_size",
                "MetricName": "其他"
            },
            {
                "Dps": [
                    {
                        "Timestamp": "1729738900",
                        "Value": "329"
                    }
                ],
                "MetricItem": "other_count",
                "MetricName": "其他"
            },
            {
                "Dps": [
                    {
                        "Timestamp": "1729738900",
                        "Value": "3273"
                    }
                ],
                "MetricItem": "total_count",
                "MetricName": "总数"
            },
            {
                "Dps": [
                    {
                        "Timestamp": "1729738900",
                        "Value": "0"
                    }
                ],
                "MetricItem": "cold_count",
                "MetricName": "冷文件"
            },
            {
                "Dps": [
                    {
                        "Timestamp": "1729738900",
                        "Value": "7210495488"
                    }
                ],
                "MetricItem": "hot_size",
                "MetricName": "热文件"
            }
        ]
    }
}
```

