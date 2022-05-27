**Example 1: 修改云数据库安全组**



Input: 

```
tccli cynosdb ModifyDBInstanceSecurityGroups --cli-unfold-argument  \
    --Zone ap-guangzhou-3 \
    --InstanceId cynosdbmysql-ins-4senc2fm \
    --SecurityGroupIds sg-ajr1jzgj
```

Output: 
```
{
    "Response": {
        "RequestId": "1a42feb9-82087f71-6a0031ac-699a92a8"
    }
}
```

