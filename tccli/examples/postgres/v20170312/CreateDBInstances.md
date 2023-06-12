**Example 1: 创建PostgreSQL实例**

新购实例

Input: 

```
tccli postgres CreateDBInstances --cli-unfold-argument  \
    --InstanceCount 1 \
    --AutoRenewFlag 1 \
    --Zone ap-guangzhou-5 \
    --DBVersion 12.4 \
    --Storage 10 \
    --Period 1 \
    --SpecCode cdb.pg.z1.2g \
    --InstanceChargeType prepaid \
    --AutoVoucher 0
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
            "postgres-xxxx"
        ],
        "BillId": "xxxxxxxxx"
    }
}
```

