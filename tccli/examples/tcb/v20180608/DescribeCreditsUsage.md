**Example 1: 查询资源点用量**

查询资源点用量

Input: 

```
tccli tcb DescribeCreditsUsage --cli-unfold-argument  \
    --StartDate 2026-02-01 \
    --EndDate 2026-03-01 \
    --EnvId ridge-work-p01-5gevsxb851439e3b
```

Output: 
```
{
    "Response": {
        "DeductValue": 39745.66,
        "HistoryDeducted": 0,
        "PackageDeductValue": 0,
        "ReportValue": 0,
        "RequestId": "b82674f3-2b57-41ff-aa75-8c77e8d5ed99"
    }
}
```

