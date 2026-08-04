**Example 1: 新购分区**



Input: 

```
tccli dlc CreatePartition --cli-unfold-argument  \
    --ActionType purchase \
    --PayMode 1 \
    --ResourceQuotaList.0.ResourceSpec.ResourceType CPU \
    --ResourceQuotaList.0.ResourceSpec.InstanceType GN10Xp \
    --ResourceQuotaList.0.ResourceSpec.BillingItem sv_dlc_standard_cu_standard_cu \
    --ResourceQuotaList.0.ResourceSpec.SpecDesc 1 GU = 1 × H20 · 0GB VRAM · 16vCPU · 160GB Memory \
    --ResourceQuotaList.0.ResourceSpec.Spec 0:1:4 \
    --ResourceQuotaList.0.ResourceSpec.GpuType V100 \
    --ResourceQuotaList.0.ResourceSpec.MaxCardPerNode 1 \
    --ResourceQuotaList.0.Quota 32 \
    --TimeSpan 1 \
    --TimeUnit m \
    --AutoRenewFlag 0 \
    --Name de**n1 \
    --Description t***2
```

Output: 
```
{
    "Response": {
        "BigDealId": "202606116********515681",
        "DealName": "202606116*******0515691",
        "RequestId": "73ee4b3e-c4a8-40f8-b2d8-f63dbfb150dd"
    }
}
```

