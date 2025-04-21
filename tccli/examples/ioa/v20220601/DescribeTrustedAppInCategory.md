**Example 1: 示例1**



Input: 

```
tccli ioa DescribeTrustedAppInCategory --cli-unfold-argument  \
    --AppCategoryId 1
```

Output: 
```
{
    "Response": {
        "Data": {
            "Page": {
                "Total": 2,
                "PageNum": 1,
                "PageSize": 10,
                "PageCount": 1
            },
            "Items": [
                {
                    "Md5": "7CB59C002E6CC82D6322CBFF125FD157",
                    "OsType": "windows",
                    "Sha256": "b67074b1378f81a6331c89acc1915fd4fef11d0255f440910c3b2c0f0a1f04bd",
                    "Status": 1,
                    "IsChosen": false,
                    "CreateTime": "2022-11-28T19:00:00+08:00",
                    "Signatures": [
                        {
                            "Signer": "Google LLC",
                            "ErrorInfo": "<nil>",
                            "RootCertName": "DigiCert Trusted Root G4",
                            "SignCertName": "Google LLC",
                            "InterCertName": "DigiCert Trusted G4 Code Signing RSA4096 SHA384 2021 CA1",
                            "SignatureStatus": "0",
                            "DigestAlgorithms": "sha256",
                            "SignatureTimestamp": "2022-11-24 05:27:27",
                            "RootCertSerialNumber": "08 ad 40 b2 60 d2 9c 4c 9f 5e cd a9 bd 93 ae d9 ",
                            "RootCertValidEndTime": "2038-01-15 20:00:00",
                            "SignCertSerialNumber": "0e 44 18 e2 de de 36 dd 29 74 c3 44 3a fb 5c e5 ",
                            "SignCertValidEndTime": "2024-07-11 07:59:59",
                            "InterCertSerialNumber": "08 ad 40 b2 60 d2 9c 4c 9f 5e cd a9 bd 93 ae d9 ",
                            "InterCertValidEndTime": "2036-04-29 07:59:59"
                        }
                    ],
                    "CheckResult": {
                        "Key": "7cb59c002e6cc82d6322cbff125fd157",
                        "Remark": "",
                        "Result": "white",
                        "Source": "电脑管家",
                        "KeyType": "md5",
                        "TreatTag": "",
                        "ThreatType": ""
                    },
                    "Manufacturer": "Copyright 2022 Google LLC. All rights reserved.",
                    "TrustedAppId": 1398,
                    "TotalInstalled": 1,
                    "TrustedAppName": "Google Chrome",
                    "SignatureDeadline": "",
                    "TrustedAppVersion": "107.0.5304.121",
                    "TrustedProcessName": "chrome.exe"
                },
                {
                    "Md5": "DE1F16A15F68FE4B8A242DC5B6EE57E8",
                    "OsType": "windows",
                    "Sha256": "bf17708bd01f59f48def134706da1da3ef91aa0097f7972fbab770f1024a99a7",
                    "Status": 1,
                    "IsChosen": false,
                    "CreateTime": "2022-11-28T18:00:00+08:00",
                    "Signatures": [
                        {
                            "Signer": "Tencent Technology(Shenzhen) Company Limited",
                            "ErrorInfo": "<nil>",
                            "RootCertName": "DigiCert Assured ID Root CA",
                            "SignCertName": "Tencent Technology(Shenzhen) Company Limited",
                            "InterCertName": "DigiCert Assured ID Code Signing CA-1",
                            "SignatureStatus": "0",
                            "DigestAlgorithms": "sha1",
                            "SignatureTimestamp": "0-00-00 00:00:00",
                            "RootCertSerialNumber": "0f a8 49 06 15 d7 00 a0 be 21 76 fd c5 ec 6d bd ",
                            "RootCertValidEndTime": "2031-11-10 08:00:00",
                            "SignCertSerialNumber": "0e 33 12 30 52 5a 25 a7 f8 10 e5 34 88 b0 aa 40 ",
                            "SignCertValidEndTime": "2024-02-23 07:59:59",
                            "InterCertSerialNumber": "0f a8 49 06 15 d7 00 a0 be 21 76 fd c5 ec 6d bd ",
                            "InterCertValidEndTime": "2026-02-10 20:00:00"
                        },
                        {
                            "Signer": "Tencent Technology(Shenzhen) Company Limited",
                            "ErrorInfo": "<nil>",
                            "RootCertName": "DigiCert Assured ID Root CA",
                            "SignCertName": "Tencent Technology(Shenzhen) Company Limited",
                            "InterCertName": "DigiCert SHA2 Assured ID Code Signing CA",
                            "SignatureStatus": "0",
                            "DigestAlgorithms": "sha256",
                            "SignatureTimestamp": "2022-11-28 17:14:03",
                            "RootCertSerialNumber": "04 09 18 1b 5f d5 bb 66 75 53 43 b5 6f 95 50 08 ",
                            "RootCertValidEndTime": "2031-11-10 08:00:00",
                            "SignCertSerialNumber": "0e a7 f6 86 bc 40 35 4a 70 f2 c2 97 c1 31 5e f6 ",
                            "SignCertValidEndTime": "2024-02-23 07:59:59",
                            "InterCertSerialNumber": "04 09 18 1b 5f d5 bb 66 75 53 43 b5 6f 95 50 08 ",
                            "InterCertValidEndTime": "2028-10-22 20:00:00"
                        }
                    ],
                    "CheckResult": {
                        "Key": "de1f16a15f68fe4b8a242dc5b6ee57e8",
                        "Remark": "",
                        "Result": "white",
                        "Source": "电脑管家",
                        "KeyType": "md5",
                        "TreatTag": "",
                        "ThreatType": ""
                    },
                    "Manufacturer": "Copyright © 2021 Tencent. All Rights Reserved.",
                    "TrustedAppId": 1396,
                    "TotalInstalled": 1,
                    "TrustedAppName": "Tencent iOA",
                    "SignatureDeadline": "",
                    "TrustedAppVersion": "107.1.13867.201",
                    "TrustedProcessName": "QQPCTray.exe"
                }
            ]
        },
        "RequestId": "88e82555-6ba2-4d5d-a3a4-f231abe067e3"
    }
}
```

