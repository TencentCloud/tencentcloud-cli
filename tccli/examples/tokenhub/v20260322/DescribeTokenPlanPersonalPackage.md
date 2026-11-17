**Example 1: 成功调用**



Input: 

```
tccli tokenhub DescribeTokenPlanPersonalPackage --cli-unfold-argument  \
    --ProductType personal
```

Output: 
```
{
    "Response": {
        "AutoRenewFlag": 1,
        "CurrentCycle": 3,
        "CycleCredits": "5000000",
        "ExpireTime": "2027-03-15T10:30:00Z",
        "PackageStatus": "active",
        "PeriodEndDate": "2026-07-15T00:00:00Z",
        "ProductType": "personal",
        "RemainCycles": 9,
        "StartTime": "2026-03-15T10:30:00Z",
        "TotalCredits": "50000000",
        "TotalCycles": 12,
        "TotalUsed": "8362150",
        "RequestId": "b78bc4eb-e3e8-4bfe-91f7-e92d83b5d030",
        "ResourceId": "pre-tp-gz-personal-202611020090241********"
    }
}
```

