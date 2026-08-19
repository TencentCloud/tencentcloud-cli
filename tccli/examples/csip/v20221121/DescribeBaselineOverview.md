**Example 1: 调用示例**



Input: 

```
tccli csip DescribeBaselineOverview --cli-unfold-argument  \
    --MemberId mem-tencent-6*************29
```

Output: 
```
{
    "Response": {
        "EnableCycleScan": true,
        "LatestScanTime": "2026-08-11T07:03:26Z",
        "ScanningTaskCount": 0,
        "Statistics": {
            "LastYearFixCount": 4,
            "NotPassItemCount": 286,
            "NotPassItemStatistic": [
                {
                    "Name": "未授权访问",
                    "NotPassCount": 3,
                    "ParentCategoryID": 3,
                    "PolicyID": 0,
                    "PolicyType": "SYSTEM"
                }
            ]
        },
        "RequestId": "1874d2ba-6376-47eb-b2e9-22f3a2378a92"
    }
}
```

