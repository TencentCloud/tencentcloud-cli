**Example 1: 设备风险评估高级版示例**



Input: 

```
tccli rce AssessDeviceRiskPremiumPro --cli-unfold-argument  \
    --DeviceToken v3:******************************************************************XquS92ODP0c0yY3E= \
    --UserIp 125.**.**.3
```

Output: 
```
{
    "Response": {
        "Data": {
            "Decision": {
                "DecisionResult": "review"
            },
            "Device": {
                "AppVersion": "1.0",
                "Brand": "OP**",
                "ClientIp": "125.**.**.3",
                "DeviceId": "1A02C*************0DF073",
                "Model": "PCK***",
                "NetworkType": "-1",
                "PackageName": "com.turingfd",
                "Platform": "2",
                "SdkBuildVersion": "90",
                "SystemVersion": "11",
                "SignToken": "-75016888***Ux8XhJzSTZI=",
                "TokenTime": "1785490616309"
            },
            "Score": {
                "RiskLabels": [
                    {
                        "Id": "101222",
                        "Reason": "Debuggable USB connection (Android)"
                    }
                ],
                "RiskLevel": 2,
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
        "RequestId": "e22f67a1-af80-4f52-8845-5cd26c883d51"
    }
}
```

