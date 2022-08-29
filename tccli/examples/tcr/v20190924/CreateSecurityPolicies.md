**Example 1: 创建实例外网访问白名单规则**



Input: 

```
tccli tcr CreateSecurityPolicies --cli-unfold-argument  \
    --RegistryId tcr-xxxx \
    --CidrBlock 192.168.0.0/24 \
    --Description aaaa
```

Output: 
```
{
    "Response": {
        "RegistryId": "XXXX",
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

