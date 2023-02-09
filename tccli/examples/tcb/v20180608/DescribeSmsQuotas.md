**Example 1: 查询免费量**

查询免费量

Input: 

```
tccli tcb DescribeSmsQuotas --cli-unfold-argument  \
    --EnvId tnt-j715s5gda
```

Output: 
```
{
    "Response": {
        "SmsFreeQuotaList": [
            {
                "FreeQuota": 1000,
                "CycleStart": "2020-01-01 23:59:59",
                "CycleEnd": "2020-02-01 23:59:59",
                "TodayUsedQuota": 0
            }
        ],
        "RequestId": "a1b9ccf2-86a7-490d-9769-a5fb6b856192"
    }
}
```

