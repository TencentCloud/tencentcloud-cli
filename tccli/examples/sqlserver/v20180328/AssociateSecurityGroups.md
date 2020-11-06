**Example 1: 安全组批量绑定云资源**



Input: 

```
tccli sqlserver AssociateSecurityGroups --cli-unfold-argument  \
    --SecurityGroupId sg-igw86yth \
    --InstanceIdSet mssql-6f4ddx2f
```

Output: 
```
{
    "Response": {
        "RequestId": "897c588d-e421-470d-9e93-468ff8eba00f"
    }
}
```

