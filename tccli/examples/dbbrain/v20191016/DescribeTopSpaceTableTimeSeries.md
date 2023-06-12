**Example 1: 获取Top表在指定时间段内的每日空间统计信息**

获取Top表在指定时间段内的每日空间统计信息。

Input: 

```
tccli dbbrain DescribeTopSpaceTableTimeSeries --cli-unfold-argument  \
    --InstanceId cdb-test \
    --Limit 2 \
    --StartDate 2020-01-01 \
    --EndDate 2020-01-01
```

Output: 
```
{
    "Response": {
        "RequestId": "d97eacb0-cebd-40b6-963b-579092454f05",
        "TopSpaceTableTimeSeries": [
            {
                "TableName": "test",
                "TableSchema": "test_bak",
                "SeriesData": {
                    "Series": [
                        {
                            "Values": [
                                0
                            ],
                            "Metric": "DataFree",
                            "Unit": "MB"
                        },
                        {
                            "Values": [
                                0.1
                            ],
                            "Metric": "DataLength",
                            "Unit": "MB"
                        },
                        {
                            "Values": [
                                0
                            ],
                            "Metric": "IndexLength",
                            "Unit": "MB"
                        },
                        {
                            "Values": [
                                0.1
                            ],
                            "Metric": "TotalLength",
                            "Unit": "MB"
                        },
                        {
                            "Values": [
                                0
                            ],
                            "Metric": "FragRatio",
                            "Unit": "%"
                        },
                        {
                            "Values": [
                                9
                            ],
                            "Metric": "TableRows",
                            "Unit": ""
                        },
                        {
                            "Values": [
                                0.1
                            ],
                            "Metric": "PhysicalFileSize",
                            "Unit": "MB"
                        }
                    ],
                    "Timestamp": [
                        1588089600
                    ]
                },
                "Engine": "InnoDB"
            },
            {
                "TableName": "test22",
                "TableSchema": "test_bak",
                "SeriesData": {
                    "Series": [
                        {
                            "Values": [
                                0
                            ],
                            "Metric": "DataFree",
                            "Unit": "MB"
                        },
                        {
                            "Values": [
                                0.1
                            ],
                            "Metric": "DataLength",
                            "Unit": "MB"
                        },
                        {
                            "Values": [
                                0
                            ],
                            "Metric": "IndexLength",
                            "Unit": "MB"
                        },
                        {
                            "Values": [
                                0.1
                            ],
                            "Metric": "TotalLength",
                            "Unit": "MB"
                        },
                        {
                            "Values": [
                                0
                            ],
                            "Metric": "FragRatio",
                            "Unit": "%"
                        },
                        {
                            "Values": [
                                6
                            ],
                            "Metric": "TableRows",
                            "Unit": ""
                        },
                        {
                            "Values": [
                                0.1
                            ],
                            "Metric": "PhysicalFileSize",
                            "Unit": "MB"
                        }
                    ],
                    "Timestamp": [
                        1588089600
                    ]
                },
                "Engine": "InnoDB"
            }
        ]
    }
}
```

