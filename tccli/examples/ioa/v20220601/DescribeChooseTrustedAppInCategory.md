**Example 1: 示例1**



Input: 

```
tccli ioa DescribeChooseTrustedAppInCategory --cli-unfold-argument  \
    --AppCategoryId 1
```

Output: 
```
{
    "Response": {
        "Data": {
            "Page": {
                "Total": 1203,
                "PageNum": 1,
                "PageSize": 10,
                "PageCount": 121
            },
            "Items": [
                {
                    "Md5": "CBF46F2EB1501E5958E6FB7E375E693D",
                    "OsType": "windows",
                    "Sha256": "9f97f15c9feeb14b1d99a1a91eed96e7b80bcad4a70de240960c7f90ee410a38",
                    "Status": 1,
                    "IsChosen": false,
                    "CreateTime": "2022-11-28T20:48:00+08:00",
                    "Signatures": [
                        {
                            "Signer": "Tencent Technology(Shenzhen) Company Limited",
                            "RootCertName": "DigiCert Assured ID Root CA",
                            "SignCertName": "Tencent Technology(Shenzhen) Company Limited",
                            "InterCertName": "DigiCert Assured ID Code Signing CA-1",
                            "SignatureStatus": "0",
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
                            "RootCertName": "DigiCert Assured ID Root CA",
                            "SignCertName": "Tencent Technology(Shenzhen) Company Limited",
                            "InterCertName": "DigiCert SHA2 Assured ID Code Signing CA",
                            "SignatureStatus": "0",
                            "SignatureTimestamp": "2022-11-25 11:22:44",
                            "RootCertSerialNumber": "04 09 18 1b 5f d5 bb 66 75 53 43 b5 6f 95 50 08 ",
                            "RootCertValidEndTime": "2031-11-10 08:00:00",
                            "SignCertSerialNumber": "0e a7 f6 86 bc 40 35 4a 70 f2 c2 97 c1 31 5e f6 ",
                            "SignCertValidEndTime": "2024-02-23 07:59:59",
                            "InterCertSerialNumber": "04 09 18 1b 5f d5 bb 66 75 53 43 b5 6f 95 50 08 ",
                            "InterCertValidEndTime": "2028-10-22 20:00:00"
                        }
                    ],
                    "CheckResult": {
                        "Key": "cbf46f2eb1501e5958e6fb7e375e693d",
                        "Remark": "",
                        "Result": "white",
                        "Source": "电脑管家",
                        "KeyType": "md5",
                        "TreatTag": "",
                        "ThreatType": ""
                    },
                    "Manufacturer": "Copyright © 2017 GitHub, Inc.",
                    "TrustedAppId": 1400,
                    "TotalInstalled": 1,
                    "TrustedAppName": "UGit",
                    "SignatureDeadline": "",
                    "TrustedAppVersion": "4.14.2.0",
                    "TrustedProcessName": "UGit.exe"
                },
                {
                    "Md5": "34B49AF7F4CD9DB825F14ABA727B648E",
                    "OsType": "windows",
                    "Sha256": "22558fdb628d666282271a45a9c7159dc9c610fd9bb61d7dd32c7f9d7cacae9d",
                    "Status": 1,
                    "IsChosen": true,
                    "CreateTime": "2022-11-28T19:30:00+08:00",
                    "Signatures": [
                        {
                            "Signer": "Tencent Technology(Shenzhen) Company Limited",
                            "RootCertName": "DigiCert Assured ID Root CA",
                            "SignCertName": "Tencent Technology(Shenzhen) Company Limited",
                            "InterCertName": "DigiCert Assured ID Code Signing CA-1",
                            "SignatureStatus": "0",
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
                            "RootCertName": "DigiCert Assured ID Root CA",
                            "SignCertName": "Tencent Technology(Shenzhen) Company Limited",
                            "InterCertName": "DigiCert SHA2 Assured ID Code Signing CA",
                            "SignatureStatus": "0",
                            "SignatureTimestamp": "2022-11-09 11:16:57",
                            "RootCertSerialNumber": "04 09 18 1b 5f d5 bb 66 75 53 43 b5 6f 95 50 08 ",
                            "RootCertValidEndTime": "2031-11-10 08:00:00",
                            "SignCertSerialNumber": "0e a7 f6 86 bc 40 35 4a 70 f2 c2 97 c1 31 5e f6 ",
                            "SignCertValidEndTime": "2024-02-23 07:59:59",
                            "InterCertSerialNumber": "04 09 18 1b 5f d5 bb 66 75 53 43 b5 6f 95 50 08 ",
                            "InterCertValidEndTime": "2028-10-22 20:00:00"
                        }
                    ],
                    "CheckResult": {
                        "Key": "34b49af7f4cd9db825f14aba727b648e",
                        "Remark": "",
                        "Result": "white",
                        "Source": "电脑管家",
                        "KeyType": "md5",
                        "TreatTag": "",
                        "ThreatType": ""
                    },
                    "Manufacturer": "Copyright (C) 2021 Tencent",
                    "TrustedAppId": 1399,
                    "TotalInstalled": 1,
                    "TrustedAppName": "WeChat",
                    "SignatureDeadline": "",
                    "TrustedAppVersion": "3.8.0.31",
                    "TrustedProcessName": "WeChat.exe"
                },
                {
                    "Md5": "7CB59C002E6CC82D6322CBFF125FD157",
                    "OsType": "windows",
                    "Sha256": "b67074b1378f81a6331c89acc1915fd4fef11d0255f440910c3b2c0f0a1f04bd",
                    "Status": 1,
                    "IsChosen": true,
                    "CreateTime": "2022-11-28T19:00:00+08:00",
                    "Signatures": [
                        {
                            "Signer": "Google LLC",
                            "RootCertName": "DigiCert Trusted Root G4",
                            "SignCertName": "Google LLC",
                            "InterCertName": "DigiCert Trusted G4 Code Signing RSA4096 SHA384 2021 CA1",
                            "SignatureStatus": "0",
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
                    "Md5": "856E7E65E146D15F2AE837D275EF26FF",
                    "OsType": "windows",
                    "Sha256": "ce2db99000f3e1fc03ae0666ec74f1e00c1f1e1f86e43dac7ab00b23cb01e0bd",
                    "Status": 1,
                    "IsChosen": false,
                    "CreateTime": "2022-11-28T18:54:00+08:00",
                    "Signatures": [
                        {
                            "Signer": "Tencent Technology(Shenzhen) Company Limited",
                            "RootCertName": "DigiCert Assured ID Root CA",
                            "SignCertName": "Tencent Technology(Shenzhen) Company Limited",
                            "InterCertName": "DigiCert Assured ID Code Signing CA-1",
                            "SignatureStatus": "0",
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
                            "RootCertName": "DigiCert Assured ID Root CA",
                            "SignCertName": "Tencent Technology(Shenzhen) Company Limited",
                            "InterCertName": "DigiCert SHA2 Assured ID Code Signing CA",
                            "SignatureStatus": "0",
                            "SignatureTimestamp": "2022-11-23 18:20:45",
                            "RootCertSerialNumber": "04 09 18 1b 5f d5 bb 66 75 53 43 b5 6f 95 50 08 ",
                            "RootCertValidEndTime": "2031-11-10 08:00:00",
                            "SignCertSerialNumber": "0e a7 f6 86 bc 40 35 4a 70 f2 c2 97 c1 31 5e f6 ",
                            "SignCertValidEndTime": "2024-02-23 07:59:59",
                            "InterCertSerialNumber": "04 09 18 1b 5f d5 bb 66 75 53 43 b5 6f 95 50 08 ",
                            "InterCertValidEndTime": "2028-10-22 20:00:00"
                        }
                    ],
                    "CheckResult": {
                        "Key": "856e7e65e146d15f2ae837d275ef26ff",
                        "Remark": "",
                        "Result": "white",
                        "Source": "电脑管家",
                        "KeyType": "md5",
                        "TreatTag": "",
                        "ThreatType": ""
                    },
                    "Manufacturer": "Copyright © 2017 GitHub, Inc.",
                    "TrustedAppId": 1397,
                    "TotalInstalled": 1,
                    "TrustedAppName": "UGit",
                    "SignatureDeadline": "",
                    "TrustedAppVersion": "4.14.1.0",
                    "TrustedProcessName": "UGit.exe"
                },
                {
                    "Md5": "DE1F16A15F68FE4B8A242DC5B6EE57E8",
                    "OsType": "windows",
                    "Sha256": "bf17708bd01f59f48def134706da1da3ef91aa0097f7972fbab770f1024a99a7",
                    "Status": 1,
                    "IsChosen": true,
                    "CreateTime": "2022-11-28T18:00:00+08:00",
                    "Signatures": [
                        {
                            "Signer": "Tencent Technology(Shenzhen) Company Limited",
                            "RootCertName": "DigiCert Assured ID Root CA",
                            "SignCertName": "Tencent Technology(Shenzhen) Company Limited",
                            "InterCertName": "DigiCert Assured ID Code Signing CA-1",
                            "SignatureStatus": "0",
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
                            "RootCertName": "DigiCert Assured ID Root CA",
                            "SignCertName": "Tencent Technology(Shenzhen) Company Limited",
                            "InterCertName": "DigiCert SHA2 Assured ID Code Signing CA",
                            "SignatureStatus": "0",
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
                },
                {
                    "Md5": "E5F6B90AF2D58D420F9214614471BCA7",
                    "OsType": "windows",
                    "Sha256": "b047bbb8c5f0ab586616e0ee41d212ab0953a0cca5ce97806f7973a28a3ecfef",
                    "Status": 1,
                    "IsChosen": false,
                    "CreateTime": "2022-11-28T17:38:00+08:00",
                    "Signatures": [
                        {
                            "Signer": "Tencent Technology(Shenzhen) Company Limited",
                            "RootCertName": "DigiCert Assured ID Root CA",
                            "SignCertName": "Tencent Technology(Shenzhen) Company Limited",
                            "InterCertName": "DigiCert Assured ID Code Signing CA-1",
                            "SignatureStatus": "0",
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
                            "RootCertName": "DigiCert Assured ID Root CA",
                            "SignCertName": "Tencent Technology(Shenzhen) Company Limited",
                            "InterCertName": "DigiCert SHA2 Assured ID Code Signing CA",
                            "SignatureStatus": "0",
                            "SignatureTimestamp": "2022-11-28 17:13:18",
                            "RootCertSerialNumber": "04 09 18 1b 5f d5 bb 66 75 53 43 b5 6f 95 50 08 ",
                            "RootCertValidEndTime": "2031-11-10 08:00:00",
                            "SignCertSerialNumber": "0e a7 f6 86 bc 40 35 4a 70 f2 c2 97 c1 31 5e f6 ",
                            "SignCertValidEndTime": "2024-02-23 07:59:59",
                            "InterCertSerialNumber": "04 09 18 1b 5f d5 bb 66 75 53 43 b5 6f 95 50 08 ",
                            "InterCertValidEndTime": "2028-10-22 20:00:00"
                        }
                    ],
                    "CheckResult": {
                        "Key": "e5f6b90af2d58d420f9214614471bca7",
                        "Remark": "",
                        "Result": "white",
                        "Source": "电脑管家",
                        "KeyType": "md5",
                        "TreatTag": "",
                        "ThreatType": ""
                    },
                    "Manufacturer": "Copyright © 2021 Tencent. All Rights Reserved.",
                    "TrustedAppId": 1394,
                    "TotalInstalled": 1,
                    "TrustedAppName": "Tencent iOA",
                    "SignatureDeadline": "",
                    "TrustedAppVersion": "107.1.13867.201",
                    "TrustedProcessName": "QQPCRtp.exe"
                },
                {
                    "Md5": "49E6A76EA7FFDE69C4E0CCFCA381D878",
                    "OsType": "windows",
                    "Sha256": "278183349fa0dc826151efed7cb9bf7ca6b61922406078b7862fda451e2dcb3b",
                    "Status": 1,
                    "IsChosen": false,
                    "CreateTime": "2022-11-28T17:38:00+08:00",
                    "Signatures": [
                        {
                            "Signer": "Tencent Technology(Shenzhen) Company Limited",
                            "RootCertName": "DigiCert Assured ID Root CA",
                            "SignCertName": "Tencent Technology(Shenzhen) Company Limited",
                            "InterCertName": "DigiCert Assured ID Code Signing CA-1",
                            "SignatureStatus": "0",
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
                            "RootCertName": "DigiCert Assured ID Root CA",
                            "SignCertName": "Tencent Technology(Shenzhen) Company Limited",
                            "InterCertName": "DigiCert SHA2 Assured ID Code Signing CA",
                            "SignatureStatus": "0",
                            "SignatureTimestamp": "2022-11-28 17:13:56",
                            "RootCertSerialNumber": "04 09 18 1b 5f d5 bb 66 75 53 43 b5 6f 95 50 08 ",
                            "RootCertValidEndTime": "2031-11-10 08:00:00",
                            "SignCertSerialNumber": "0e a7 f6 86 bc 40 35 4a 70 f2 c2 97 c1 31 5e f6 ",
                            "SignCertValidEndTime": "2024-02-23 07:59:59",
                            "InterCertSerialNumber": "04 09 18 1b 5f d5 bb 66 75 53 43 b5 6f 95 50 08 ",
                            "InterCertValidEndTime": "2028-10-22 20:00:00"
                        }
                    ],
                    "CheckResult": {
                        "Key": "49e6a76ea7ffde69c4e0ccfca381d878",
                        "Remark": "",
                        "Result": "white",
                        "Source": "电脑管家",
                        "KeyType": "md5",
                        "TreatTag": "",
                        "ThreatType": ""
                    },
                    "Manufacturer": "Copyright © 2021 Tencent. All Rights Reserved.",
                    "TrustedAppId": 1395,
                    "TotalInstalled": 1,
                    "TrustedAppName": "Tencent iOA",
                    "SignatureDeadline": "",
                    "TrustedAppVersion": "107.1.13867.201",
                    "TrustedProcessName": "TpkUpdate.exe"
                },
                {
                    "Md5": "D9A09861473B35EF2FB2156C37FDEB03",
                    "OsType": "windows",
                    "Sha256": "311449af7d9090c8e83a4097984741209b0f0ce61b2470e7f9a1f84e830473dc",
                    "Status": 1,
                    "IsChosen": false,
                    "CreateTime": "2022-11-28T17:34:00+08:00",
                    "Signatures": [
                        {
                            "Signer": "Tencent Technology(Shenzhen) Company Limited",
                            "RootCertName": "DigiCert Assured ID Root CA",
                            "SignCertName": "Tencent Technology(Shenzhen) Company Limited",
                            "InterCertName": "DigiCert Assured ID Code Signing CA-1",
                            "SignatureStatus": "0",
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
                            "RootCertName": "DigiCert Assured ID Root CA",
                            "SignCertName": "Tencent Technology(Shenzhen) Company Limited",
                            "InterCertName": "DigiCert SHA2 Assured ID Code Signing CA",
                            "SignatureStatus": "0",
                            "SignatureTimestamp": "2022-11-28 17:13:52",
                            "RootCertSerialNumber": "04 09 18 1b 5f d5 bb 66 75 53 43 b5 6f 95 50 08 ",
                            "RootCertValidEndTime": "2031-11-10 08:00:00",
                            "SignCertSerialNumber": "0e a7 f6 86 bc 40 35 4a 70 f2 c2 97 c1 31 5e f6 ",
                            "SignCertValidEndTime": "2024-02-23 07:59:59",
                            "InterCertSerialNumber": "04 09 18 1b 5f d5 bb 66 75 53 43 b5 6f 95 50 08 ",
                            "InterCertValidEndTime": "2028-10-22 20:00:00"
                        }
                    ],
                    "CheckResult": {
                        "Key": "d9a09861473b35ef2fb2156c37fdeb03",
                        "Remark": "",
                        "Result": "white",
                        "Source": "电脑管家",
                        "KeyType": "md5",
                        "TreatTag": "",
                        "ThreatType": ""
                    },
                    "Manufacturer": "Copyright © 2021 Tencent. All Rights Reserved.",
                    "TrustedAppId": 1393,
                    "TotalInstalled": 1,
                    "TrustedAppName": "Tencent iOA",
                    "SignatureDeadline": "",
                    "TrustedAppVersion": "107.1.13867.201",
                    "TrustedProcessName": "qmdl.exe"
                },
                {
                    "Md5": "1574787E0BF829269940942CE39AB940",
                    "OsType": "windows",
                    "Sha256": "209b8eb979710687935a33e4b02746ec97745b619fc1ca631b7abb3fd5cba16e",
                    "Status": 1,
                    "IsChosen": false,
                    "CreateTime": "2022-11-28T17:32:00+08:00",
                    "Signatures": [
                        {
                            "Signer": "Tencent Technology(Shenzhen) Company Limited",
                            "RootCertName": "DigiCert Assured ID Root CA",
                            "SignCertName": "Tencent Technology(Shenzhen) Company Limited",
                            "InterCertName": "DigiCert Assured ID Code Signing CA-1",
                            "SignatureStatus": "0",
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
                            "RootCertName": "DigiCert Assured ID Root CA",
                            "SignCertName": "Tencent Technology(Shenzhen) Company Limited",
                            "InterCertName": "DigiCert SHA2 Assured ID Code Signing CA",
                            "SignatureStatus": "0",
                            "SignatureTimestamp": "2022-11-28 17:13:54",
                            "RootCertSerialNumber": "04 09 18 1b 5f d5 bb 66 75 53 43 b5 6f 95 50 08 ",
                            "RootCertValidEndTime": "2031-11-10 08:00:00",
                            "SignCertSerialNumber": "0e a7 f6 86 bc 40 35 4a 70 f2 c2 97 c1 31 5e f6 ",
                            "SignCertValidEndTime": "2024-02-23 07:59:59",
                            "InterCertSerialNumber": "04 09 18 1b 5f d5 bb 66 75 53 43 b5 6f 95 50 08 ",
                            "InterCertValidEndTime": "2028-10-22 20:00:00"
                        }
                    ],
                    "CheckResult": {
                        "Key": "1574787e0bf829269940942ce39ab940",
                        "Remark": "",
                        "Result": "white",
                        "Source": "电脑管家",
                        "KeyType": "md5",
                        "TreatTag": "",
                        "ThreatType": ""
                    },
                    "Manufacturer": "",
                    "TrustedAppId": 1392,
                    "TotalInstalled": 1,
                    "TrustedAppName": "",
                    "SignatureDeadline": "",
                    "TrustedAppVersion": "",
                    "TrustedProcessName": "QMUploadEx.exe"
                },
                {
                    "Md5": "BB2B6D916CAAFD8F5884366FB9E957C8",
                    "OsType": "windows",
                    "Sha256": "5d46979a44313f60807b1b168f33dc386f22bb16de9c34ac1f349f6b94c7884a",
                    "Status": 1,
                    "IsChosen": false,
                    "CreateTime": "2022-11-28T17:32:00+08:00",
                    "Signatures": [
                        {
                            "Signer": "Tencent Technology(Shenzhen) Company Limited",
                            "RootCertName": "DigiCert Assured ID Root CA",
                            "SignCertName": "Tencent Technology(Shenzhen) Company Limited",
                            "InterCertName": "DigiCert Assured ID Code Signing CA-1",
                            "SignatureStatus": "0",
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
                            "RootCertName": "DigiCert Assured ID Root CA",
                            "SignCertName": "Tencent Technology(Shenzhen) Company Limited",
                            "InterCertName": "DigiCert SHA2 Assured ID Code Signing CA",
                            "SignatureStatus": "0",
                            "SignatureTimestamp": "2022-11-28 17:13:55",
                            "RootCertSerialNumber": "04 09 18 1b 5f d5 bb 66 75 53 43 b5 6f 95 50 08 ",
                            "RootCertValidEndTime": "2031-11-10 08:00:00",
                            "SignCertSerialNumber": "0e a7 f6 86 bc 40 35 4a 70 f2 c2 97 c1 31 5e f6 ",
                            "SignCertValidEndTime": "2024-02-23 07:59:59",
                            "InterCertSerialNumber": "04 09 18 1b 5f d5 bb 66 75 53 43 b5 6f 95 50 08 ",
                            "InterCertValidEndTime": "2028-10-22 20:00:00"
                        }
                    ],
                    "CheckResult": {
                        "Key": "bb2b6d916caafd8f5884366fb9e957c8",
                        "Remark": "",
                        "Result": "white",
                        "Source": "电脑管家",
                        "KeyType": "md5",
                        "TreatTag": "",
                        "ThreatType": ""
                    },
                    "Manufacturer": "Copyright (C) 1998-2020 Tencent. All Rights Reserved",
                    "TrustedAppId": 1391,
                    "TotalInstalled": 1,
                    "TrustedAppName": "Tencent TenioDL",
                    "SignatureDeadline": "",
                    "TrustedAppVersion": "2.0.15.1002",
                    "TrustedProcessName": "TenioDL.exe"
                }
            ]
        },
        "RequestId": "824fbf72-2363-4f1d-b74d-e997bcca7b2c"
    }
}
```

