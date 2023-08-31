**Example 1: 示例**

无

Input: 

```
tccli csip DescribeSearchBugInfo --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Data": {
            "StateCode": "xx",
            "DataBug": [
                {
                    "Id": 1,
                    "PatchId": "xx",
                    "VULName": "xx",
                    "Level": "xx",
                    "CVSSScore": "xx",
                    "CVEId": "xx",
                    "Tag": "xx",
                    "VULCategory": 1,
                    "ImpactOs": "xx",
                    "ImpactCOMPENT": "xx",
                    "ImpactVersion": "xx",
                    "Reference": "xx",
                    "VULDescribe": "xx",
                    "Fix": "xx",
                    "ProSupport": 1,
                    "IsPublish": 1,
                    "ReleaseTime": "xx",
                    "CreateTime": "xx",
                    "UpdateTime": "xx",
                    "SubCategory": "xx"
                }
            ],
            "DataAsset": [
                {
                    "AppID": "xx",
                    "CVEId": "xx",
                    "IsScan": 0,
                    "InfluenceAsset": 0,
                    "NotRepairAsset": 0,
                    "NotProtectAsset": 0,
                    "TaskId": "xx",
                    "TaskPercent": 0,
                    "TaskTime": 0,
                    "ScanTime": "xx"
                }
            ],
            "VSSScan": true,
            "CWPScan": "xx",
            "CFWPatch": "xx",
            "WafPatch": 0,
            "CWPFix": 0
        },
        "ReturnCode": 0,
        "ReturnMsg": "xx",
        "RequestId": "xx"
    }
}
```

