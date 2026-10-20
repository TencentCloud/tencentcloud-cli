**Example 1: 示例1**



Input: 

```
tccli ioa ModifyDeliveryStrategy --cli-unfold-argument  \
    --Name deliver \
    --LogTypes 040201000000 \
    --Type 0 \
    --ConfigId 1 \
    --Description dlp \
    --Enabled True \
    --ID 0
```

Output: 
```
{
    "Response": {
        "RequestId": "724b28d6-a182-4c9d-bffb-c7c92c4403fe"
    }
}
```

