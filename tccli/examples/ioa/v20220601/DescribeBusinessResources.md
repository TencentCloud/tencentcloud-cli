**Example 1: 查询资源列表**



Input: 

```
tccli ioa DescribeBusinessResources --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Data": {
            "Items": [
                {
                    "APISecretId": 0,
                    "AccessType": 0,
                    "AreaId": 8,
                    "AreaName": "sjntest",
                    "BackendPath": "",
                    "BackendScheme": "",
                    "CertificateId": 0,
                    "CnameStatus": 0,
                    "ConnectorGroupId": "d9unlkvpf1kbvg5841og",
                    "ConnectorGroupName": "国际站test",
                    "ConnectorGroupType": "native",
                    "CreateTime": "2026-08-13 17:39:59",
                    "CustomDomain": "",
                    "CustomHost": "",
                    "DependentAddr": "",
                    "DetectInfo": "**",
                    "DetectState": 1,
                    "DetectTime": "2026-08-13 17:39:59",
                    "DirectConn": 0,
                    "DisableFront": 0,
                    "DomainSuffix": "260210447.global.renwox.com",
                    "EnableDependentAddr": 0,
                    "FrontHost": "",
                    "FrontPath": "",
                    "FrontPort": 0,
                    "FrontScheme": "",
                    "Levels": 5000,
                    "Protocol": 2,
                    "ReachableState": 0,
                    "ReachableTime": "",
                    "Remark": "",
                    "SSLCertId": "",
                    "ServiceAddress": "*.qq.com",
                    "ServiceId": 15,
                    "ServiceName": "测sjntest",
                    "ServicePort": "all",
                    "ServiceType": "domain",
                    "SmartGateIds": [
                        6
                    ],
                    "SmartGateNames": "smartgate;",
                    "UpdateTime": "2026-08-13 17:40:00",
                    "WebGwNoAuth": 1,
                    "WebGwResourceType": 0
                }
            ],
            "Page": {
                "PageCount": 1,
                "PageNum": 1,
                "PageSize": 10,
                "Total": 6
            }
        },
        "RequestId": "00fbdd4b-9f36-431e-8c68-cb811c931c53"
    }
}
```

