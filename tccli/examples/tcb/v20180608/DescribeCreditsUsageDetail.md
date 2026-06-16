**Example 1: 不返回用量明细**



Input: 

```
tccli tcb DescribeCreditsUsageDetail --cli-unfold-argument  \
    --Modules EKS \
    --StartDate 2025-12-21 \
    --EndDate 2025-12-23 \
    --NeedUsageDetails False \
    --EnvId yntest-1gudy58n050fbe21
```

Output: 
```
{
    "Response": {
        "Usages": [
            {
                "CreditsValue": 10.41,
                "DeductValue": 10.41,
                "EnvId": "yntest-1gudy58n050fbe21",
                "MetricUsageDetail": [
                    {
                        "BillingCycleType": "daily",
                        "CreditsValue": 10.41,
                        "DeductValue": 10.41,
                        "MetricName": "Flux",
                        "PackageDeductValue": 0,
                        "ReportValue": 0,
                        "ResourceType": "NAT",
                        "Unit": "Byte",
                        "Value": 13976221,
                        "ValueDetailList": []
                    }
                ],
                "Module": "EKS",
                "PackageDeductValue": 0,
                "ReportValue": 0
            }
        ],
        "RequestId": "9c4f04f0-b5cf-4e13-ada1-30a80fefe714"
    }
}
```

**Example 2: 返回用量明细**

NeedUsageDetails为 true返回用量明细，且 StartDate和EndDate为同一天

Input: 

```
tccli tcb DescribeCreditsUsageDetail --cli-unfold-argument  \
    --Modules EKS \
    --StartDate 2025-12-31 \
    --EndDate 2025-12-31 \
    --NeedUsageDetails True \
    --EnvId yntest-1gudy58n050fbe21
```

Output: 
```
{
    "Response": {
        "Usages": [
            {
                "CreditsValue": 13.06,
                "DeductValue": 13.06,
                "EnvId": "yntest-1gudy58n050fbe21",
                "MetricUsageDetail": [
                    {
                        "BillingCycleType": "daily",
                        "CreditsValue": 13.06,
                        "DeductValue": 13.06,
                        "MetricName": "Flux",
                        "PackageDeductValue": 0,
                        "ReportValue": 0,
                        "ResourceType": "NAT",
                        "Unit": "Byte",
                        "Value": 17559586,
                        "ValueDetailList": [
                            {
                                "CalcTime": "2025-12-30 23:00:00",
                                "CreditsValue": 0.65,
                                "DeductValue": 0.65,
                                "PackageDeductValue": 0,
                                "RawValue": 869001,
                                "ReportValue": 0
                            }
                        ]
                    }
                ],
                "Module": "EKS",
                "PackageDeductValue": 0,
                "ReportValue": 0
            }
        ],
        "RequestId": "eabff6d3-363e-499f-8654-194508286361"
    }
}
```

