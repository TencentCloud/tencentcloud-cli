**Example 1: 修改站点的独立 DDoS 防护**

修改站点的独立 DDoS 防护。

Input: 

```
tccli teo ModifyDDoSProtection --cli-unfold-argument  \
    --ZoneId zone-2jaltqbdhq37 \
    --DDoSProtection.ProtectionOption protect_specified_domains \
    --DDoSProtection.DomainDDoSProtections.0.Domain www.example.com \
    --DDoSProtection.DomainDDoSProtections.0.Switch on
```

Output: 
```
{
    "Response": {
        "RequestId": "1362c269-9931-4b12-b148-3d1df0818600"
    }
}
```

