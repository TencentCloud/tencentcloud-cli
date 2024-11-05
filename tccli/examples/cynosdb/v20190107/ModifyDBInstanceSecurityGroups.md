**Example 1: 修改实例绑定安全组**

修改实例绑定安全组

Input: 

```
tccli cynosdb ModifyDBInstanceSecurityGroups --cli-unfold-argument  \
    --InstanceId cynosdbmysql-j8ynfcpgj \
    --SecurityGroupIds sg-mnbv \
    --Zone ap-guangzhou-3
```

Output: 
```
{
    "Response": {
        "RequestId": "48fa5cf5-77db-4e32-90ef-22c71ed95f51"
    }
}
```

