**Example 1: 查询模型路由资源包列表**

查询模型路由资源包列表

Input: 

```
tccli clb DescribeModelRouterResourcePackages --cli-unfold-argument  \
    --ModelRouterResourcePackageIds cmrcredit-k2800toa8g6hjar \
    --SortBy asc \
    --Filters.0.Name status \
    --Filters.0.Values 0
```

Output: 
```
{
    "Response": {
        "ModelRouterResourcePackageSet": [
            {
                "AutoPurchaseFlag": 0,
                "CapacityRemain": "100",
                "CapacityRemainPrecise": "100",
                "CapacitySize": "100",
                "CapacitySizePrecise": "100",
                "CreateTime": "2026-04-09 13:10:02",
                "DeductionEndTime": "2029-04-09 13:10:00",
                "DeductionStartTime": "2026-04-09 13:10:01",
                "ExpiredTime": "",
                "ModelRouterResourcePackageId": "cmrcredit-k2800toa8g6hjar",
                "Status": 0
            }
        ],
        "TotalCount": 1,
        "TotalDosage": 100,
        "RequestId": "9983568b-1d4f-426d-a5dc-e86367d8ab78"
    }
}
```

