**Example 1: DescribePlatformCreditsUsageDetail**



Input: 

```
tccli tcb DescribePlatformCreditsUsageDetail --cli-unfold-argument  \
    --Modules PostgreSQL \
    --StartDate 2026-09-11 \
    --EndDate 2026-10-11 \
    --NeedUsageDetails True \
    --PlatformId pf-35zc08k5rfxtq
```

Output: 
```
{
    "Response": {
        "Usages": [
            {
                "CreditsValue": 0,
                "DeductValue": 0,
                "MetricUsageDetail": [
                    {
                        "BillingCycleType": "hourly",
                        "CreditsValue": 0,
                        "DeductValue": 0,
                        "MetricName": "HourlyCU",
                        "PackageDeductValue": 0,
                        "ReportValue": 0,
                        "ResourceType": "PostgreSQL",
                        "Unit": "核秒",
                        "Value": 0,
                        "ValueDetailList": []
                    }
                ],
                "Module": "PostgreSQL",
                "PackageDeductValue": 0,
                "PlatformId": "pf-35zc08k5rfxtq",
                "ReportValue": 0
            }
        ],
        "RequestId": "c14de03b-f26f-41e4-b3e4-014055424d11"
    }
}
```

