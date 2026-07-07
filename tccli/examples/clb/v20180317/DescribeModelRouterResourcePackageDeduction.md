**Example 1: 查询模型资源包抵扣详情**

查询模型资源包抵扣详情

Input: 

```
tccli clb DescribeModelRouterResourcePackageDeduction --cli-unfold-argument  \
    --DeductionTimeBegin 2026-04-06 10:23:00 \
    --DeductionTimeEnd 2026-04-10 20:23:00 \
    --ModelRouterResourcePackageId cmrcredit-k2800toa8gc7far
```

Output: 
```
{
    "Response": {
        "ModelRouterResourcePackageDeductionSet": [
            {
                "ActualDosage": "100",
                "AfterDeductionRemain": "0",
                "BeforeDeductionRemain": "100",
                "DeductionTime": "2026-04-09 19:30:00",
                "Dosage": "2.2675737",
                "EndTime": "2026-04-09 14:22:00",
                "ModelRouterId": "cmr-a1b2c3d1",
                "ModelRouterResourcePackageId": "cmrcredit-k2800toa8gc7far",
                "StartTime": "2026-04-09 14:21:00"
            }
        ],
        "TotalCount": 1,
        "RequestId": "687e97f0-43d9-46bb-9f32-4f486c38d9b2"
    }
}
```

