**Example 1: Getting the number of resource instances in region**



Input: 

```
tccli dayu DescribleRegionCount --cli-unfold-argument  \
    --Business bgpip
```

Output: 
```
{
    "Response": {
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397",
        "RegionList": [
            {
                "Count": 5,
                "Region": "gz",
                "RegionV3": "ap-guangzhou"
            },
            {
                "Count": 4,
                "Region": "sh",
                "RegionV3": "ap-shanghai"
            }
        ]
    }
}
```

