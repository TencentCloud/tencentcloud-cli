**Example 1: 创建kms实例**



Input: 

```
tccli kms CreateKmsInstance --cli-unfold-argument  \
    --InstanceChargeType PREPAID \
    --ProductVersion professional \
    --InstanceChargePrepaid.Period 1 \
    --InstanceChargePrepaid.RenewFlag 1 \
    --ClientToken 9a4d46f4-c223-4652-af87-610d21a606aq \
    --Tags.0.TagKey department \
    --Tags.0.TagValue development
```

Output: 
```
{
    "Response": {
        "BillId": "",
        "DealName": "20260921********0569371",
        "InstanceId": "KMS-Pre*******nkr28g",
        "RequestId": "54d52fdc-fa20-4efa-87e8-3092246a0a26"
    }
}
```

