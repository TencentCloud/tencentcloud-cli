**Example 1: 查询报告概览**



Input: 

```
tccli bsca DescribeReportOverview --cli-unfold-argument  \
    --AnalysisId 34b0e422-c7be-404a-8861-a543af8393c8
```

Output: 
```
{
    "Response": {
        "AnalysisName": "AnalysisName",
        "AnalysisType": "GENERIC",
        "FileName": "demo.img",
        "FileSize": 20408884,
        "UpdatedTime": "2021-10-29T11:52:40Z",
        "CVECount": {
            "CriticalCount": 1,
            "HighCount": 2,
            "MediumCount": 3,
            "LowCount": 4
        },
        "SensitivePrivateKeyCount": 1,
        "SensitiveURIPasswordCount": 2,
        "SensitiveIPCount": {
            "TotalCount": 102,
            "TopList": [
                {
                    "Name": "192.168.1.1",
                    "Count": 10
                },
                {
                    "Name": "192.168.1.2",
                    "Count": 8
                },
                {
                    "Name": "192.168.1.3",
                    "Count": 5
                }
            ]
        },
        "SensitiveURICount": {
            "TotalCount": 103,
            "TopList": [
                {
                    "Name": "a.com",
                    "Count": 18
                },
                {
                    "Name": "b.com",
                    "Count": 15
                },
                {
                    "Name": "c.com",
                    "Count": 8
                }
            ]
        },
        "SensitiveMailCount": {
            "TotalCount": 102,
            "TopList": [
                {
                    "Name": "qq.com",
                    "Count": 10
                },
                {
                    "Name": "tencent.com",
                    "Count": 8
                },
                {
                    "Name": "gmail.com",
                    "Count": 5
                }
            ]
        },
        "ComponentCount": [
            {
                "ComponentName": "openssh v1.6",
                "CVECount": {
                    "CriticalCount": 3,
                    "HighCount": 3,
                    "MediumCount": 3,
                    "LowCount": 0
                }
            },
            {
                "ComponentName": "libpng v2.05",
                "CVECount": {
                    "CriticalCount": 3,
                    "HighCount": 3,
                    "MediumCount": 2,
                    "LowCount": 0
                }
            },
            {
                "ComponentName": "libpng v2.03",
                "CVECount": {
                    "CriticalCount": 3,
                    "HighCount": 3,
                    "MediumCount": 1,
                    "LowCount": 0
                }
            },
            {
                "ComponentName": "libpng v2.06",
                "CVECount": {
                    "CriticalCount": 3,
                    "HighCount": 3,
                    "MediumCount": 0,
                    "LowCount": 0
                }
            },
            {
                "ComponentName": "openssh v3.10.132",
                "CVECount": {
                    "CriticalCount": 3,
                    "HighCount": 0,
                    "MediumCount": 0,
                    "LowCount": 0
                }
            }
        ],
        "RequestId": "eacfb401-a322-493a-8e36-83b295412345"
    }
}
```

