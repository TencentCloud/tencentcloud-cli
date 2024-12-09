**Example 1: CreateReadOnlyDBInstance**

创建只读实例

Input: 

```
tccli postgres CreateReadOnlyDBInstance --cli-unfold-argument  \
    --InstanceCount 1 \
    --AutoRenewFlag 1 \
    --Zone ap-guangzhou-2 \
    --MasterDBInstanceId Postgres-testmaster \
    --DBVersion 9.3.5 \
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
        "BillId": "20241205591002398481191",
        "DBInstanceIdSet": [
            "pgro-kdkdkx68"
        ],
        "DealNames": [
            "20241205591002398481181"
        ],
        "RequestId": "5ce80f91-a285-4378-8340-332ab4bfe9cd"
    }
}
```

