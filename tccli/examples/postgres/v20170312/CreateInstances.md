**Example 1: 创建12.4版本的PostgreSQL实例**

创建12.4版本中最新内核版的PostgreSQL实例

Input: 

```
tccli postgres CreateInstances --cli-unfold-argument  \
    --SpecCode cdb.pg.z1.2g \
    --Storage 10 \
    --InstanceCount 1 \
    --Period 1 \
    --InstanceChargeType prepaid \
    --Zone ap-guangzhou-2 \
    --DBVersion 12.4 \
    --AutoVoucher 0 \
    --AutoRenewFlag 1 \
    --Charset UTF8 \
    --AdminName test2313 \
    --AdminPassword ' xxxxxxx'
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
            "postgres-xxxxx"
        ],
        "BillId": "123"
    }
}
```

**Example 2: 创建12版本中最新内核版本的PostgreSQL实例**

创建12版本中最新内核版本的PostgreSQL实例（跨可用区）

Input: 

```
tccli postgres CreateInstances --cli-unfold-argument  \
    --SpecCode cdb.pg.z1.2g \
    --Storage 10 \
    --InstanceCount 1 \
    --Period 1 \
    --InstanceChargeType prepaid \
    --Zone ap-guangzhou-2 \
    --DBMajorVersion 12 \
    --AutoVoucher 0 \
    --AutoRenewFlag 1 \
    --Charset UTF8 \
    --AdminName test2313 \
    --AdminPassword ' xxxxxxx' \
    --DBNodeSet.0.Role Primary \
    --DBNodeSet.0.Zone ap-guangzhou-2 \
    --DBNodeSet.1.Role Standby \
    --DBNodeSet.1.Zone ap-guangzhou-3
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
            "postgres-xxxxx"
        ],
        "BillId": "123"
    }
}
```

**Example 3: 创建指定内核版本号的PostgreSQL实例**

创建内核版本号为v12.4_r1.0版本的PostgreSQL实例

Input: 

```
tccli postgres CreateInstances --cli-unfold-argument  \
    --SpecCode cdb.pg.z1.2g \
    --Storage 10 \
    --InstanceCount 1 \
    --Period 1 \
    --InstanceChargeType prepaid \
    --Zone ap-guangzhou-2 \
    --DBKernelVersion v12.4_r1.0 \
    --AutoVoucher 0 \
    --AutoRenewFlag 1 \
    --Charset UTF8 \
    --AdminName test2313 \
    --AdminPassword ' xxxxxxx'
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
            "postgres-xxxxx"
        ],
        "BillId": "123"
    }
}
```

