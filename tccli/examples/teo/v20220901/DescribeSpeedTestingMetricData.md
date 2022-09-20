**Example 1: 查询站点拨测结果**



Input: 

```
tccli teo DescribeSpeedTestingMetricData --cli-unfold-argument  \
    --ZoneId zone-2805lqj66rf6
```

Output: 
```
{
    "Response": {
        "RequestId": "f9a45aa8-01ab-40c0-ac2d-e61178fd2c51",
        "SpeedTestingMetricData": {
            "OriginSpeedTestingInfo": [
                {
                    "SpeedTestingStatistics": {
                        "DocumentFinishTime": 0,
                        "FirstMeaningfulPaint": 0,
                        "LoadTime": 0,
                        "OverallDownloadSpeed": 0.0,
                        "FileDownloadTime": 0,
                        "FirstContentfulPaint": 0,
                        "ResponseTime": 0,
                        "RenderTime": 0,
                        "TcpConnectionTime": 0
                    },
                    "SpeedTestingConfig": {
                        "Url": "https://www.tencent.com/",
                        "Connectivity": "Cable",
                        "UA": "Chrome,PC",
                        "TaskType": 0
                    },
                    "TestId": "test-id",
                    "StatusCode": 0
                }
            ],
            "SpeedTestingStatus": {
                "Tls": true,
                "Url": "https://www.tencent.com/",
                "CreatedOn": "2020-09-22T00:00:00+00:00",
                "Connectivity": "Cable",
                "UA": "Chrome,PC",
                "StatusCode": 0,
                "TimedOut": true,
                "Reachable": true
            },
            "OriginLoadTime": 0,
            "ZoneId": "zone-2805lqj66rf6",
            "ProxyLoadTime": 0,
            "ProxySpeedTestingInfo": [
                {
                    "SpeedTestingStatistics": {
                        "DocumentFinishTime": 0,
                        "FirstMeaningfulPaint": 0,
                        "LoadTime": 0,
                        "OverallDownloadSpeed": 0.0,
                        "FileDownloadTime": 0,
                        "FirstContentfulPaint": 0,
                        "ResponseTime": 0,
                        "RenderTime": 0,
                        "TcpConnectionTime": 0
                    },
                    "SpeedTestingConfig": {
                        "Url": "https://www.tencent.com/",
                        "Connectivity": "Cable",
                        "UA": "Chrome,PC",
                        "TaskType": 0
                    },
                    "TestId": "test-dadfcsas",
                    "StatusCode": 0
                }
            ],
            "OptimizeAction": [
                {
                    "Connectivity": "Cable",
                    "Ratio": 0,
                    "Name": "name",
                    "Value": 0
                }
            ],
            "ZoneName": "zone.com"
        }
    }
}
```

