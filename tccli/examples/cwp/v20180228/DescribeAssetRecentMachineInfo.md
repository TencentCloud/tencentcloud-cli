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
        "RequestId": "xx",
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

