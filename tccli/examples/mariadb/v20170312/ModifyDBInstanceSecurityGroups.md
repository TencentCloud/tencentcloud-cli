**Example 1: 示例1 修改云数据库安全组**



Input: 

```
tccli mariadb ModifyDBInstanceSecurityGroups --cli-unfold-argument  \
    --InstanceId tdsql-eb2w7dto \
    --Product mariadb \
    --SecurityGroupIds sg-ajr1jzgj
```

Output: 
```
{
    "Response": {
        "RequestId": "31a60135-7057-47ae-8fd3-7a0617deca38"
    }
}
```

