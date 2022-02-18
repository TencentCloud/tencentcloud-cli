**Example 1: 查询实例克隆需要的最小规格**



Input: 

```
tccli postgres DescribeCloneDBInstanceSpec --cli-unfold-argument  \
    --DBInstanceId postgres-apzvwncr \
    --RecoveryTargetTime '2021-12-24 03:41:50'
```

Output: 
```
{
    "Response": {
        "RequestId": "08fdf411-5d39-44f2-8e1d-a58ee60b237d",
        "MinSpecCode": "cdb.pg.sh1.2g",
        "MinStorage": 10
    }
}
```

