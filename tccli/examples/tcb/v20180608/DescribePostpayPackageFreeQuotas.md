**Example 1: 获取后付费免费额度**

获取后付费免费额度 

Input: 

```
tccli tcb DescribePostpayPackageFreeQuotas --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "PackageFreeQuotaInfos": [
            {
                "ResourceType": "COS",
                "ResourceMetric": "ReadRequests",
                "FreeQuota": 150,
                "MetricUnit": "万次",
                "DeductType": "sum-month",
                "FreeQuotaType": "basic"
            },
            {
                "ResourceType": "COS",
                "ResourceMetric": "WriteRequests",
                "FreeQuota": 60,
                "MetricUnit": "万次",
                "DeductType": "sum-month",
                "FreeQuotaType": "basic"
            },
            {
                "ResourceType": "COS",
                "ResourceMetric": "Capacity",
                "FreeQuota": 5,
                "MetricUnit": "GB",
                "DeductType": "totalize",
                "FreeQuotaType": "basic"
            },
            {
                "ResourceType": "COS",
                "ResourceMetric": "Flux",
                "FreeQuota": 5,
                "MetricUnit": "GB",
                "DeductType": "sum-month",
                "FreeQuotaType": "basic"
            },
            {
                "ResourceType": "CDN",
                "ResourceMetric": "Flux",
                "FreeQuota": 5,
                "MetricUnit": "GB",
                "DeductType": "sum-month",
                "FreeQuotaType": "basic"
            },
            {
                "ResourceType": "SCF",
                "ResourceMetric": "MemoryUse",
                "FreeQuota": 40000,
                "MetricUnit": "GBs",
                "DeductType": "sum-month",
                "FreeQuotaType": "basic"
            },
            {
                "ResourceType": "SCF",
                "ResourceMetric": "Outflow",
                "FreeQuota": 1,
                "MetricUnit": "GB",
                "DeductType": "sum-month",
                "FreeQuotaType": "basic"
            },
            {
                "ResourceType": "FLEXDB",
                "ResourceMetric": "Capacity",
                "FreeQuota": 2,
                "MetricUnit": "GB",
                "DeductType": "totalize",
                "FreeQuotaType": "basic"
            },
            {
                "ResourceType": "FLEXDB",
                "ResourceMetric": "ReadRequests",
                "FreeQuota": 5,
                "MetricUnit": "万次",
                "DeductType": "sum-day",
                "FreeQuotaType": "basic"
            },
            {
                "ResourceType": "FLEXDB",
                "ResourceMetric": "WriteRequests",
                "FreeQuota": 3,
                "MetricUnit": "万次",
                "DeductType": "sum-day",
                "FreeQuotaType": "basic"
            },
            {
                "ResourceType": "HOSTING",
                "ResourceMetric": "Capacity",
                "FreeQuota": 5120,
                "MetricUnit": "GB",
                "DeductType": "totalize",
                "FreeQuotaType": "basic"
            }
        ],
        "RequestId": "a1b9ccf2-86a7-490d-9769-a5fb6b856192"
    }
}
```

