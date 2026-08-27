**Example 1: 新购分区**



Input: 

```
tccli dlc CreatePartition --cli-unfold-argument  \
    --ActionType purchase \
    --PayMode 1 \
    --ResourceQuotaList.0.ResourceSpec.BillingItem sv_dlc_standard_cu_standard_cu \
    --ResourceQuotaList.0.Quota 32 \
    --TimeSpan 1 \
    --TimeUnit m \
    --Name my_part \
    --Description This is my part
```

Output: 
```
{
    "Response": {
        "BigDealId": "20260826585023461942451",
        "DealName": "20260826585023461942461",
        "RequestId": "7cf550ab-e4b1-4e45-9391-a5df1ba1515a"
    }
}
```

