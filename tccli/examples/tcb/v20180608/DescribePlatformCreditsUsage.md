**Example 1: DescribePlatformCreditsUsage**



Input: 

```
tccli tcb DescribePlatformCreditsUsage --cli-unfold-argument  \
    --StartDate 2026-09-01 \
    --EndDate 2026-09-30 \
    --PlatformId pf-3iovc1ty3nug3
```

Output: 
```
{
    "Response": {
        "DailyList": [
            {
                "Date": "2026-09-01",
                "DeductValue": 0,
                "OriginCredits": 0,
                "PackageDeductValue": 0,
                "ReportValue": 0
            }
        ],
        "DeductValueCount": 8579960,
        "PackageDeductValueCount": 0,
        "ReportValueCount": 123625.5,
        "RequestId": "19c3312e-4267-40c6-8066-387a30492ab2"
    }
}
```

