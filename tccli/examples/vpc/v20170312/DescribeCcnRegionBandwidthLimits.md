**Example 1: 查询一个CCN各地域出带宽上限**

查询一个CCN各地域出带宽上限

Input: 

```
tccli vpc DescribeCcnRegionBandwidthLimits --cli-unfold-argument  \
    --CcnId ccn-gree226l
```

Output: 
```
{
    "Response": {
        "CcnRegionBandwidthLimitSet": [
            {
                "BandwidthLimit": 50,
                "Region": "ap-guangzhou"
            },
            {
                "BandwidthLimit": 10000,
                "Region": "ap-beijing"
            },
            {
                "BandwidthLimit": 2000,
                "Region": "ap-shanghai"
            }
        ],
        "RequestId": "9c53ff69-1bb6-4c89-adbb-812233a85acc"
    }
}
```

