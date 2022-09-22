**Example 1: 创建12.4版本的PostgreSQL实例**

创建12.4版本中最新内核版的PostgreSQL实例

Input: 

```
tccli postgres CreateInstances --cli-unfold-argument  \
    --InstanceCount 1 \
    --AutoRenewFlag 1 \
    --AdminName test2313 \
    --Zone ap-guangzhou-2 \
    --AdminPassword  xxxxxxx \
    --DBVersion 12.4 \
    --DBEngine postgresql \
    --Storage 10 \
    --Period 1 \
    --SpecCode cdb.pg.z1.2g \
    --InstanceChargeType prepaid \
    --AutoVoucher 0 \
    --Charset UTF8
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
    --InstanceCount 1 \
    --AutoRenewFlag 1 \
    --DBMajorVersion 12 \
    --Zone ap-guangzhou-2 \
    --AdminPassword  xxxxxxx \
    --Charset UTF8 \
    --Storage 10 \
    --Period 1 \
    --SpecCode cdb.pg.z1.2g \
    --InstanceChargeType prepaid \
    --AutoVoucher 0 \
    --DBNodeSet.0.Role Standby \
    --DBNodeSet.0.Zone ap-guangzhou-3 \
    --DBNodeSet.1.Role Primary \
    --DBNodeSet.1.Zone ap-guangzhou-2 \
    --AdminName test2313
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
    --InstanceCount 1 \
    --AutoRenewFlag 1 \
    --AdminName test2313 \
    --Zone ap-guangzhou-2 \
    --AdminPassword  xxxxxxx \
    --Charset UTF8 \
    --Storage 10 \
    --Period 1 \
    --SpecCode cdb.pg.z1.2g \
    --DBKernelVersion v12.4_r1.0 \
    --DBEngine postgresql \
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
            "postgres-xxxxx"
        ],
        "BillId": "123"
    }
}
```

