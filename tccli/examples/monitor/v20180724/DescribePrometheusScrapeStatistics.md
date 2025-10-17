**Example 1: 获取实例采集速率**

获取实例采集速率

Input: 

```
tccli monitor DescribePrometheusScrapeStatistics --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Total": 0,
        "InstanceResults": [
            {
                "InstanceId": "prom-ejhf",
                "ScrapedRate": 1.4,
                "Clusters": [
                    {
                        "ClusterID": "cls-oebw",
                        "ScrapedRate": 0.1,
                        "Jobs": [
                            {
                                "JobName": "test-job",
                                "ScrapedRate": 0.1,
                                "Metrics": [
                                    {
                                        "MetricName": "countMetric",
                                        "SamplesRate": 3.4,
                                        "ScrapedRate": 0.1,
                                        "IsRecommended": true
                                    }
                                ]
                            }
                        ],
                        "SamplesRate": 3.4
                    }
                ],
                "Global": [
                    {
                        "ClusterID": "non-cluster",
                        "ScrapedRate": 1.3,
                        "Jobs": [
                            {
                                "JobName": "ceph-test",
                                "ScrapedRate": 1.3,
                                "Metrics": [
                                    {
                                        "MetricName": "upTime",
                                        "SamplesRate": 2.1,
                                        "ScrapedRate": 1.3,
                                        "IsRecommended": true
                                    }
                                ]
                            }
                        ],
                        "SamplesRate": 2.1
                    }
                ],
                "SamplesRate": 5.5
            }
        ],
        "RequestId": "6fc6a7e8-2a5c-40f2-bf0e-8cb807fa665d"
    }
}
```

