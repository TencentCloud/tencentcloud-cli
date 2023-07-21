**Example 1: 克隆实例**

原实例误删数据时，可用克隆实例功能恢复。

Input: 

```
tccli postgres CloneDBInstance --cli-unfold-argument  \
    --VpcId vpc-2ot3acw1 \
    --AutoRenewFlag 1 \
    --DBInstanceId postgres-abcd1234 \
    --RecoveryTargetTime 2021-12-25 01:27:35 \
    --Storage 10 \
    --Period 1 \
    --AutoVoucher 0 \
    --InstanceChargeType prepaid \
    --SpecCode cdb.pg.z1.2g \
    --SubnetId subnet-ppv9iw34 \
    --DBNodeSet.0.Role Standby \
    --DBNodeSet.0.Zone ap-guangzhou-3 \
    --DBNodeSet.1.Role Primary \
    --DBNodeSet.1.Zone ap-guangzhou-3
```

Output: 
```
{
    "Response": {
        "RequestId": "6ace8140-6b9e-4e81-a8ad-ef3f92b2aa90",
        "DealName": "20211225711000768276461",
        "BillId": "20211225711000768276471",
        "DBInstanceId": "postgres-xxxx"
    }
}
```

