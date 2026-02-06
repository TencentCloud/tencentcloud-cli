**Example 1: 示例 1**



Input: 

```
tccli billing SetRenewal --cli-unfold-argument  \
    --ProductCode p_cos \
    --RegionCode ap-others \
    --InstanceId std_storage-20240902185001827926251-1 \
    --RenewFlag NOTIFY_AND_MANUAL_RENEW \
    --RenewPeriod 3 \
    --RenewPeriodUnit m
```

Output: 
```
{
    "Response": {
        "InstanceList": [],
        "RequestId": "6a5c90f0-10e8-4586-97f7-abafa2e46dcf"
    }
}
```

