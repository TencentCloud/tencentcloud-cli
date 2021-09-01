**Example 1: 安全组批量解绑云资源**



Input: 

```
tccli sqlserver DisassociateSecurityGroups --cli-unfold-argument  \
    --SecurityGroupId sg-igw86yth \
    --InstanceIdSet mssql-6f4ddx2f
```

Output: 
```
{
    "Response": {
        "RequestId": "595838fa-07e2-4a6d-9957-4ad7825749fc"
    }
}
```

