**Example 1: 克隆实例**



Input: 

```
tccli postgres CloneDBInstance --cli-unfold-argument  \
    --DBInstanceId postgres-abcd1234 \
    --SpecCode cdb.pg.z1.2g \
    --Storage 10 \
    --Period 1 \
    --InstanceChargeType prepaid \
    --AutoVoucher 0 \
    --AutoRenewFlag 1 \
    --DBNodeSet.0.Role Primary \
    --DBNodeSet.0.Zone ap-guangzhou-3 \
    --DBNodeSet.1.Role Standby \
    --DBNodeSet.1.Zone ap-guangzhou-3 \
    --RecoveryTargetTime '2021-12-25 01:27:35' \
    --VpcId vpc-2ot3acw1 \
    --SubnetId subnet-ppv9iw34
```

Output: 
```
{
    "Response": {
        "RequestId": "6ace8140-6b9e-4e81-a8ad-ef3f92b2aa90",
        "DealName": "20211225711000768276461",
        "BillId": "20211225711000768276471"
    }
}
```

