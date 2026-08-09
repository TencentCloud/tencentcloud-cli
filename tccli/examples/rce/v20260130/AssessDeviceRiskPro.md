**Example 1: 设备风险评估基础版示例**



Input: 

```
tccli rce AssessDeviceRiskPro --cli-unfold-argument  \
    --DeviceToken v3:**************************************************u58Tcp7u042WRcZBER/N/w== \
    --UserIp 183.**.**.16
```

Output: 
```
{
    "Response": {
        "Data": {
            "Device": {
                "AppVersion": "1.0",
                "Brand": "OP**",
                "ClientIp": "183.**.**.16",
                "DeviceId": "350C54************54E940",
                "Model": "PCK****",
                "NetworkType": "0",
                "PackageName": "com.******",
                "Platform": "2",
                "SdkBuildVersion": "90",
                "SystemVersion": "11",
                "SignToken": "-75016888***Ux8XhJzSTZI=",
                "TokenTime": "1785490616309"
            },
            "Score": {
                "RiskLabels": [
                    {
                        "Id": "101208",
                        "Reason": "Debugging Mode Enabled (Android)"
                    }
                ],
                "RiskLevel": 3,
                "RiskScore": 150
            },
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
            }
        },
        "RequestId": "e86e9de7-435c-4a0a-847b-237867dacb8d"
    }
}
```

