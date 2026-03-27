**Example 1: 将单可用区实例调整为多可用区**



Input: 

```
tccli mongodb ModifyInstanceAz --cli-unfold-argument  \
    --InstanceId cmgo-p9d**** \
    --PrimaryNodeZone ap-guangzhou-2 \
    --HiddenNodeZone ap-guangzhou-3 \
    --SecondaryNodeZone ap-guangzhou-4 \
    --ReadonlyNodeZone None \
    --InMaintenance None
```

Output: 
```
{
    "Response": {
        "DealId": "2025080702700316299****",
        "RequestId": "87f3a779-9b2e-475f-bcf5-966cffbbbe9f"
    }
}
```

