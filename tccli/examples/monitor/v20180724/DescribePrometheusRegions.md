**Example 1: 列出 Prometheus 服务所有可用的区域和可用区**



Input: 

```
tccli monitor DescribePrometheusRegions --cli-unfold-argument  \
    --PayMode 3
```

Output: 
```
{
    "Response": {
        "RegionSet": [
            {
                "RegionState": 1,
                "Region": "ap-guangzhou",
                "RegionId": 1,
                "RegionName": "广州",
                "RegionShortName": "gz",
                "Area": "华南地区",
                "RegionPayMode": 3
            }
        ],
        "RequestId": "xx"
    }
}
```

