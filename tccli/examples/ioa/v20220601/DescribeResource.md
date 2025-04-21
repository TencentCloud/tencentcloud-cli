**Example 1: 查询资源组下的资源**

查询资源组下的资源

Input: 

```
tccli ioa DescribeResource --cli-unfold-argument  \
    --AreaId 9
```

Output: 
```
{
    "Response": {
        "Data": {
            "Items": [
                {
                    "AccessType": 0,
                    "AreaId": 9,
                    "AreaName": "group1",
                    "BackendPath": "",
                    "BackendScheme": "",
                    "CertificateId": 0,
                    "CnameStatus": 0,
                    "CustomDomain": "",
                    "CustomHost": "",
                    "DirectConn": 0,
                    "DisableFront": 0,
                    "EnableFlag": 1,
                    "FrontHost": "",
                    "FrontPath": "",
                    "FrontPort": 0,
                    "FrontScheme": "",
                    "Id": 16,
                    "Itime": "2023-01-30T11:16:08.931279+08:00",
                    "Levels": 5000,
                    "Protocol": 2,
                    "SecretId": 0,
                    "ServiceAddress": "*.qq.com",
                    "ServiceName": "QQ",
                    "ServicePort": "all",
                    "ServiceType": "",
                    "SmartGates": "{21}",
                    "Utime": "2023-03-27T15:40:09.086887+08:00",
                    "WebGwResourceType": 0
                },
                {
                    "AccessType": 0,
                    "AreaId": 9,
                    "AreaName": "group1",
                    "BackendPath": "",
                    "BackendScheme": "",
                    "CertificateId": 0,
                    "CnameStatus": 0,
                    "CustomDomain": "",
                    "CustomHost": "",
                    "DirectConn": 0,
                    "DisableFront": 0,
                    "EnableFlag": 1,
                    "FrontHost": "",
                    "FrontPath": "",
                    "FrontPort": 0,
                    "FrontScheme": "",
                    "Id": 15,
                    "Itime": "2023-01-30T11:10:47.894308+08:00",
                    "Levels": 5000,
                    "Protocol": 3,
                    "SecretId": 0,
                    "ServiceAddress": "*.baidu.com",
                    "ServiceName": "baidu",
                    "ServicePort": "all",
                    "ServiceType": "",
                    "SmartGates": "{21}",
                    "Utime": "2023-03-27T15:41:12.523411+08:00",
                    "WebGwResourceType": 0
                },
                {
                    "AccessType": 0,
                    "AreaId": 9,
                    "AreaName": "group1",
                    "BackendPath": "",
                    "BackendScheme": "",
                    "CertificateId": 0,
                    "CnameStatus": 0,
                    "CustomDomain": "",
                    "CustomHost": "",
                    "DirectConn": 0,
                    "DisableFront": 0,
                    "EnableFlag": 1,
                    "FrontHost": "",
                    "FrontPath": "",
                    "FrontPort": 0,
                    "FrontScheme": "",
                    "Id": 14,
                    "Itime": "2023-01-30T11:01:04.804683+08:00",
                    "Levels": 5000,
                    "Protocol": 3,
                    "SecretId": 0,
                    "ServiceAddress": "www.tencent.com",
                    "ServiceName": "tencent",
                    "ServicePort": "all",
                    "ServiceType": "",
                    "SmartGates": "{21}",
                    "Utime": "2023-03-30T16:23:25.382117+08:00",
                    "WebGwResourceType": 0
                },
                {
                    "AccessType": 0,
                    "AreaId": 9,
                    "AreaName": "group1",
                    "BackendPath": "",
                    "BackendScheme": "",
                    "CertificateId": 0,
                    "CnameStatus": 0,
                    "CustomDomain": "",
                    "CustomHost": "",
                    "DirectConn": 2,
                    "DisableFront": 0,
                    "EnableFlag": 1,
                    "FrontHost": "",
                    "FrontPath": "",
                    "FrontPort": 0,
                    "FrontScheme": "",
                    "Id": 40,
                    "Itime": "2023-04-07T16:35:34.966082+08:00",
                    "Levels": 0,
                    "Protocol": 2,
                    "SecretId": 0,
                    "ServiceAddress": "www.baidu.com",
                    "ServiceName": "web-baidu",
                    "ServicePort": "443",
                    "ServiceType": "",
                    "SmartGates": "{}",
                    "Utime": "2023-04-07T16:35:34.966082+08:00",
                    "WebGwResourceType": 0
                }
            ],
            "Page": {
                "PageCount": 0,
                "PageNum": 0,
                "PageSize": 0,
                "Total": 4
            }
        },
        "RequestId": "17c7aa32-cf15-455c-bc90-940fd95d6fe2"
    }
}
```

