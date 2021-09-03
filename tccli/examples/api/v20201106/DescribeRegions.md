**Example 1: 请求例子**



Input: 

```
tccli api DescribeRegions --cli-unfold-argument  \
    --Product xx
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "RegionSet": [
            {
                "Region": "ap-guangzhou",
                "RegionName": "华南地区(广州)",
                "RegionState": "AVAILABLE"
            }
        ],
        "RequestId": "f252873e-fbbd-4651-ba75-205c7e5ba6fc"
    }
}
```

