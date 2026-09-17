**Example 1: 新购后付费分区**

后付费（按量计费）新购，返回 DealName + BillId，BigDealId 为空。Quota 固定传 0，TimeSpan/TimeUnit 为 3600/s

Input: 

```
tccli dlc CreatePartition --cli-unfold-argument  \
    --ActionType purchase \
    --PayMode 0 \
    --ResourceQuotaList.0.ResourceSpec.BillingItem sv_dlc_standard_cu_standard_cu \
    --ResourceQuotaList.0.Quota 0 \
    --TimeSpan 3600 \
    --TimeUnit s \
    --Name test-postpay-pool
```

Output: 
```
{
    "Response": {
        "DealName": "20260812501023354768101",
        "BigDealId": "",
        "BillId": "20260812160000002684725323617409",
        "RequestId": "a60d786d-5c7f-47b5-9296-394699e580e3"
    }
}
```

**Example 2: 新购预付费分区**

预付费（包年包月）新购，返回 DealName + BigDealId，BillId 为空

Input: 

```
tccli dlc CreatePartition --cli-unfold-argument  \
    --ActionType purchase \
    --PayMode 1 \
    --ResourceQuotaList.0.ResourceSpec.BillingItem sv_dlc_standard_cu_standard_cu \
    --ResourceQuotaList.0.Quota 32 \
    --TimeSpan 1 \
    --TimeUnit m \
    --Name hughe0805
```

Output: 
```
{
    "Response": {
        "BigDealId": "20260812501023354768091",
        "DealName": "20260812501023354768101",
        "BillId": "",
        "RequestId": "35716323-e368-4b93-9d01-3511cfcb74ed"
    }
}
```

