**Example 1: 示例**



Input: 

```
tccli csip DescribeNotifyAssetConfig --cli-unfold-argument  \
    --Modules Alert
```

Output: 
```
{
    "Response": {
        "Items": [
            {
                "AssetRange": 2,
                "CloudTags": [],
                "ExcludedInstanceIds": [],
                "InstanceIds": [
                    "ins-********"
                ],
                "Module": "Alert",
                "SubModule": "BRUTE_FORCE",
                "TagIds": [],
                "TotalCount": 10
            }
        ],
        "RequestId": "02f6385b-5b8e-450d-b77b-b727370d5d15"
    }
}
```

