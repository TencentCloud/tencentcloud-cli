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
                "Value": 0,
                "Key": "xx",
                "Desc": "xx"
            }
        ],
        "LiveList": [
            {
                "Value": 0,
                "Key": "xx",
                "Desc": "xx"
            }
        ],
        "TotalList": [
            {
                "Value": 0,
                "Key": "xx",
                "Desc": "xx"
            }
        ],
        "RequestId": "a8658ae6-0cd1-47f0-99b0-f144f01e9066",
        "OfflineList": [
            {
                "Value": 0,
                "Key": "xx",
                "Desc": "xx"
            }
        ]
    }
}
```

