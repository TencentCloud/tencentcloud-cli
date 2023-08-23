**Example 1: 修改云数据库安全组**

修改安全组

Input: 

```
tccli cynosdb ModifyDBInstanceSecurityGroups --cli-unfold-argument  \
    --InstanceId cynosdbmysql-ins-lkj \
    --SecurityGroupIds sg-mnbv \
    --Zone ap-guangzhou-3
```

Output: 
```
{
    "Response": {
        "RequestId": "abc"
    }
}
```

