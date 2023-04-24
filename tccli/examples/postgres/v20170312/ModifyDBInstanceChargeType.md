**Example 1: postgres-apzvwncr修改计费模式**

postgres-apzvwncr修改计费模式为包年包月

Input: 

```
tccli postgres ModifyDBInstanceChargeType --cli-unfold-argument  \
    --DBInstanceId postgres-apzvwncr \
    --InstanceChargeType PREPAID \
    --AutoRenewFlag 0 \
    --AutoVoucher 0 \
    --Period 1
```

Output: 
```
{
    "Response": {
        "RequestId": "08fdf411-5d39-44f2-8e1d-a58ee60b237d",
        "DealName": "201806181256"
    }
}
```

