**Example 1: 安全组批量绑定云资源**



Input: 

```
tccli cynosdb AssociateSecurityGroups --cli-unfold-argument  \
    --Zone ap-guangzhou \
    --InstanceIds cynosdbmysql-xxxxxxxx \
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

