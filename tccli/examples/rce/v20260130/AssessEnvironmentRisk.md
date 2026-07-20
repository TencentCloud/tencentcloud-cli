**Example 1: 环境风险评估示例**



Input: 

```
tccli rce AssessEnvironmentRisk --cli-unfold-argument  \
    --UserIp 100.*****.0
```

Output: 
```
{
    "Response": {
        "Data": {
            "Environment": {
                "Location": {
                    "City": "Guarapari",
                    "Country": "BR",
                    "District": "Todos os Santos",
                    "Latitude": "***.***136",
                    "Longitude": "***.**36",
                    "Region": "Espírito Santo",
                    "Timezone": "UTC-3",
                    "ZipCode": "29200-080"
                },
                "Network": {
                    "ASN": "Telefonica",
                    "ISP": "18881",
                    "IsAnycast": false,
                    "IsCloudService": false,
                    "IsCompany": false,
                    "IsDNS": false,
                    "IsDynamic": false,
                    "IsEducation": false,
                    "IsEgress": false,
                    "IsGateway": false,
                    "IsInfrastructure": false,
                    "IsInstitution": false,
                    "IsMXServer": false,
                    "IsMobile": false,
                    "IsReserved": false,
                    "IsResidence": false,
                    "Organization": "Telefonica"
                }
            },
            "Score": {
                "RiskLabels": [
                    {
                        "Id": "201003",
                        "Reason": "Proxy"
                    },
                    {
                        "Id": "201004",
                        "Reason": "Scanning Activity"
                    }
                ],
                "RiskLevel": 4
            }
        },
        "RequestId": "099c98e6-0a70-41f5-a68d-54e57ee9e534"
    }
}
```

