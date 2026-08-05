**Example 1: 分区变配**



Input: 

```
tccli dlc ModifyPartition --cli-unfold-argument  \
    --PartitionCode dlc-p-c******l \
    --TargetResourceQuotaList.0.ResourceSpec.ResourceType CPU \
    --TargetResourceQuotaList.0.ResourceSpec.InstanceType GN10Xp \
    --TargetResourceQuotaList.0.ResourceSpec.BillingItem sv_dlc_standard_cu_standard_cu \
    --TargetResourceQuotaList.0.ResourceSpec.SpecDesc 1 GU = 1 × H20 · 0GB VRAM · 16vCPU · 160GB Memory \
    --TargetResourceQuotaList.0.ResourceSpec.Spec 0:1:4 \
    --TargetResourceQuotaList.0.ResourceSpec.GpuType V100 \
    --TargetResourceQuotaList.0.ResourceSpec.MaxCardPerNode 1 \
    --TargetResourceQuotaList.0.Quota 64 \
    --PayMode 1 \
    --TimeSpan 1 \
    --TimeUnit m
```

Output: 
```
{
    "Response": {
        "BigDealId": "202606116**********3061",
        "DealName": "202606116*********43071",
        "RequestId": "b7c939e9-434e-45df-8d36-8566d7843038"
    }
}
```

