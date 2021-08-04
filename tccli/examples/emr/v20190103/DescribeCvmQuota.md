**Example 1: 获取账户的CVM配额**



Input: 

```
tccli emr DescribeCvmQuota --cli-unfold-argument  \
    --ClusterId emr-xxxxxxxx \
    --ZoneId 100002
```

Output: 
```
{
    "Response": {
        "PostPaidQuotaSet": [
            {
                "UsedQuota": 0,
                "RemainingQuota": 288,
                "TotalQuota": 288,
                "Zone": "ap-guangzhou-1"
            }
        ],
        "SpotPaidQuotaSet": [
            {
                "UsedQuota": 0,
                "RemainingQuota": 244,
                "TotalQuota": 244,
                "Zone": "ap-guangzhou-1"
            }
        ],
        "EksQuotaSet": [
            {
                "NodeType": "TASK",
                "Cpu": 12000,
                "Memory": 32000000,
                "Number": 12
            }
        ],
        "RequestId": "f0f11d21-6d0d-4f73-9177-8ae4ec456068"
    }
}
```

