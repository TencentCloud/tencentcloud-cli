**Example 1: 创建PostgreSQL实例**



Input: 

```
tccli postgres CreateDBInstances --cli-unfold-argument  \
    --SpecCode cdb.pg.z1.2g \
    --Storage 10 \
    --InstanceCount 1 \
    --Period 1 \
    --InstanceChargeType prepaid \
    --Zone ap-guangzhou-2 \
    --DBVersion 12.4 \
    --AutoVoucher 0 \
    --AutoRenewFlag 1
```

Output: 
```
{
    "Response": {
        "RequestId": "6ace8140-6b9e-4e81-a8ad-ef3f92b2aa90",
        "DealNames": [
            "20180119110001"
        ],
        "DBInstanceIdSet": [
            "123"
        ],
        "BillId": "123"
    }
}
```

