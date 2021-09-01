**Example 1: 修改云数据库安全组**



Input: 

```
tccli sqlserver ModifyDBInstanceSecurityGroups --cli-unfold-argument  \
    --InstanceId mssql-6f4ddx2f \
    --SecurityGroupIdSet sg-igw86yth
```

Output: 
```
{
    "Response": {
        "RequestId": "9ae37be8-05dc-4d5f-90b9-ea9efdc353e9"
    }
}
```

