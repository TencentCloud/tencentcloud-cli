**Example 1: 创建只读实例，使用校验模式**

创建只读实例，指定主实例为postgres-abcdef，只校验不实际发起创建

Input: 

```
tccli postgres CreateReadOnlyDBInstance --cli-unfold-argument  \
    --DBVersion 12.22 \
    --InstanceChargeType POSTPAID_BY_HOUR \
    --InstanceCount 1 \
    --MasterDBInstanceId postgres-abcdef \
    --Period 1 \
    --ProjectId 1 \
    --ReadOnlyGroupId  \
    --SecurityGroupIds sg-iwnfp51z \
    --SpecCode pg.it.small2 \
    --Storage 100 \
    --SubnetId subnet-1i9huswn \
    --VpcId vpc-8btfafeo \
    --Zone ap-beijing-4
```

Output: 
```
{
    "Response": {
        "BillId": "",
        "DBInstanceIdSet": [],
        "DealNames": [],
        "RequestId": "e0726ee5-3f5f-414c-9976-17e94dd0023e"
    }
}
```

**Example 2: 创建只读实例**

创建只读实例，指定主实例为postgres-abcdef，实际发起创建

Input: 

```
tccli postgres CreateReadOnlyDBInstance --cli-unfold-argument  \
    --DBVersion 12.22 \
    --InstanceChargeType POSTPAID_BY_HOUR \
    --InstanceCount 1 \
    --MasterDBInstanceId postgres-abcdef \
    --Period 1 \
    --ProjectId 1 \
    --ReadOnlyGroupId  \
    --SecurityGroupIds sg-iwnfp51z \
    --SpecCode pg.it.small2 \
    --Storage 100 \
    --SubnetId subnet-1i9huswn \
    --VpcId vpc-8btfafeo \
    --Zone ap-beijing-4
```

Output: 
```
{
    "Response": {
        "BillId": "2701077795",
        "DBInstanceIdSet": [],
        "DealNames": [
            "20251009929109544409421"
        ],
        "RequestId": "f3b13348-be76-4631-8d2f-0c8da1e07958"
    }
}
```

