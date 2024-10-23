**Example 1: 获取主机概况趋势**



Input: 

```
tccli cwp DescribeAssetRecentMachineInfo --cli-unfold-argument  \
    --BeginDate 2020-09-22 \
    --EndDate 2020-09-22
```

Output: 
```
{
    "Response": {
        "RiskList": [
            {
                "Value": 10,
                "Key": "App",
                "Desc": "softwares",
                "NewCount": 0
            }
        ],
        "LiveList": [
            {
                "Value": 20,
                "Key": "frame",
                "Desc": "",
                "NewCount": 0
            }
        ],
        "TotalList": [
            {
                "Value": 30,
                "Key": "Web",
                "Desc": "web app",
                "NewCount": 0
            }
        ],
        "RequestId": "a8658ae6-0cd1-47f0-99b0-f144f01e9066",
        "OfflineList": [
            {
                "Value": 40,
                "Key": "total",
                "Desc": "total",
                "NewCount": 0
            }
        ]
    }
}
```

