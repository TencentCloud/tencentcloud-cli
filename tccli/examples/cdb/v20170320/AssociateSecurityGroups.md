**Example 1: 安全组批量绑定云资源**



Input: 

```
tccli cdb AssociateSecurityGroups --cli-unfold-argument  \
    --SecurityGroupId sg-ajr1jzgj \
    --InstanceIds cdb-eb2w7dto
```

Output: 
```
{
    "Response": {
        "RequestId": "1a42feb9-82087f71-6a0031ac-699a92a8"
    }
}
```

