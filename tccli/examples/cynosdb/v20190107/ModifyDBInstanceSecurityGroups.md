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
        "RequestId": "abc"
    }
}
```

