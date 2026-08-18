**Example 1: 工作空间转换计费模式**

按量转包年包月

Input: 

```
tccli thpc ModifyWorkspacesChargeType --cli-unfold-argument  \
    --SpaceIds wks-azkpgmz5 \
    --SpaceChargeType PREPAID \
    --DryRun False \
    --SpaceChargePrepaid.Period 1 \
    --SpaceChargePrepaid.RenewFlag NOTIFY_AND_MANUAL_RENEW
```

Output: 
```
{
    "Response": {
        "RequestId": "9f80f09b-f157-4ba6-9197-6622a1195c9a"
    }
}
```

