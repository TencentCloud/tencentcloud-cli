**Example 1: 创建实例公网访问白名单策略**



Input: 

```
tccli tcr CreateSecurityPolicy --cli-unfold-argument  \
    --RegistryId tcr-dg284imq \
    --CidrBlock 192.168.0.0/24 \
    --Description desc
```

Output: 
```
{
    "Response": {
        "RegistryId": "tcr-dg284imq",
        "RequestId": "ed971e07-75c0-4236-8e4f-f98967a6f713"
    }
}
```

