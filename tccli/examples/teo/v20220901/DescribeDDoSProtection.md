**Example 1: 获取站点的独立 DDoS 防护信息**

获取站点的独立 DDoS 防护信息。

Input: 

```
tccli teo DescribeDDoSProtection --cli-unfold-argument  \
    --ZoneId zone-2jaltqbdhq37
```

Output: 
```
{
    "Response": {
        "RequestId": "1362c269-9931-4b12-b148-3d1df0818600",
        "DDoSProtection": {
            "ProtectionOption": "protect_specified_domains",
            "DomainDDoSProtections": [
                {
                    "Domain": "www.example.com",
                    "Switch": "on"
                }
            ],
            "SharedCNAMEDDoSProtections": [
                {
                    "Domain": "a.example.com",
                    "Switch": "off"
                }
            ]
        }
    }
}
```

