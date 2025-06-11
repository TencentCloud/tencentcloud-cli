**Example 1: 查看软件详情列表**



Input: 

```
tccli ioa DescribeSoftwareInformation --cli-unfold-argument  \
    --Mid 123
```

Output: 
```
{
    "Response": {
        "RequestId": "ada4c0d5-2e2d-4264-93b9-c067a4ddb62e",
        "Data": {
            "Items": [],
            "Page": {
                "Total": 0,
                "PageCount": 0,
                "PageSize": 1000,
                "PageNum": 1
            }
        }
    }
}
```

**Example 2: 获取设备安装软件信息**

获取设备安装的软件数据

Input: 

```
tccli ioa DescribeSoftwareInformation --cli-unfold-argument  \
    --Mid B454307F6CA03B56E0CFEC44EABF93BB67E56D6F
```

Output: 
```
{
    "Response": {
        "Data": {
            "Items": [
                {
                    "CorpName": "",
                    "Id": 19396,
                    "InstallDate": "2025/04/03",
                    "Mid": "B454307F6CA03B56E0CFEC44EABF93BB67E56D6F",
                    "Name": "微信",
                    "PiracyRisk": 0,
                    "SoftwareId": 19396,
                    "Version": "3.9.12.51"
                },
                {
                    "CorpName": "",
                    "Id": 23532,
                    "InstallDate": "2025/04/16",
                    "Mid": "B454307F6CA03B56E0CFEC44EABF93BB67E56D6F",
                    "Name": "Google Chrome",
                    "PiracyRisk": 0,
                    "SoftwareId": 23532,
                    "Version": "135.0.7049.95"
                },
                {
                    "CorpName": "",
                    "Id": 23452,
                    "InstallDate": "2025/04/16",
                    "Mid": "B454307F6CA03B56E0CFEC44EABF93BB67E56D6F",
                    "Name": "Mozilla Firefox (x64 zh-CN)",
                    "PiracyRisk": 0,
                    "SoftwareId": 23452,
                    "Version": "137.0.2"
                },
                {
                    "CorpName": "",
                    "Id": 19198,
                    "InstallDate": "2025/03/31",
                    "Mid": "B454307F6CA03B56E0CFEC44EABF93BB67E56D6F",
                    "Name": "Adobe Acrobat Reader DC MUI",
                    "PiracyRisk": 2,
                    "SoftwareId": 19198,
                    "Version": "15.007.20033"
                },
                {
                    "CorpName": "",
                    "Id": 19639,
                    "InstallDate": "2025/04/01",
                    "Mid": "B454307F6CA03B56E0CFEC44EABF93BB67E56D6F",
                    "Name": "企业微信",
                    "PiracyRisk": 0,
                    "SoftwareId": 19639,
                    "Version": "4.1.36.6004"
                },
                {
                    "CorpName": "",
                    "Id": 19197,
                    "InstallDate": "2025/03/31",
                    "Mid": "B454307F6CA03B56E0CFEC44EABF93BB67E56D6F",
                    "Name": "Java 8 Update 441",
                    "PiracyRisk": 0,
                    "SoftwareId": 19197,
                    "Version": "8.0.4410.7"
                },
                {
                    "CorpName": "",
                    "Id": 19059,
                    "InstallDate": "2024/12/13",
                    "Mid": "B454307F6CA03B56E0CFEC44EABF93BB67E56D6F",
                    "Name": "运维审计系统 单点登录组件 2.0",
                    "PiracyRisk": 0,
                    "SoftwareId": 19059,
                    "Version": "2.0"
                },
                {
                    "CorpName": "",
                    "Id": 18422,
                    "InstallDate": "2024/04/10",
                    "Mid": "B454307F6CA03B56E0CFEC44EABF93BB67E56D6F",
                    "Name": "软件管理",
                    "PiracyRisk": 0,
                    "SoftwareId": 18422,
                    "Version": "3.1.1442.301"
                },
                {
                    "CorpName": "",
                    "Id": 18595,
                    "InstallDate": "2025/03/27",
                    "Mid": "B454307F6CA03B56E0CFEC44EABF93BB67E56D6F",
                    "Name": "腾讯 iOA",
                    "PiracyRisk": 0,
                    "SoftwareId": 18595,
                    "Version": "210.3.25981.62001"
                },
                {
                    "CorpName": "",
                    "Id": 21450,
                    "InstallDate": "2025/04/11",
                    "Mid": "B454307F6CA03B56E0CFEC44EABF93BB67E56D6F",
                    "Name": "向日葵远程控制",
                    "PiracyRisk": 0,
                    "SoftwareId": 21450,
                    "Version": "15.8.3.19819"
                },
                {
                    "CorpName": "",
                    "Id": 18725,
                    "InstallDate": "2024/04/10",
                    "Mid": "B454307F6CA03B56E0CFEC44EABF93BB67E56D6F",
                    "Name": "企业版软件管家",
                    "PiracyRisk": 0,
                    "SoftwareId": 18725,
                    "Version": "101.1.169.1"
                },
                {
                    "CorpName": "",
                    "Id": 19057,
                    "InstallDate": "2024/03/19",
                    "Mid": "B454307F6CA03B56E0CFEC44EABF93BB67E56D6F",
                    "Name": "Wireshark 3.4.6 64-bit",
                    "PiracyRisk": 0,
                    "SoftwareId": 19057,
                    "Version": "3.4.6"
                },
                {
                    "CorpName": "",
                    "Id": 19195,
                    "InstallDate": "2025/03/28",
                    "Mid": "B454307F6CA03B56E0CFEC44EABF93BB67E56D6F",
                    "Name": "ToDesk",
                    "PiracyRisk": 0,
                    "SoftwareId": 19195,
                    "Version": "4.7.6.3"
                },
                {
                    "CorpName": "",
                    "Id": 19055,
                    "InstallDate": "2025/04/11",
                    "Mid": "B454307F6CA03B56E0CFEC44EABF93BB67E56D6F",
                    "Name": "TeamViewer",
                    "PiracyRisk": 0,
                    "SoftwareId": 19055,
                    "Version": "15.46.5"
                },
                {
                    "CorpName": "",
                    "Id": 19054,
                    "InstallDate": "2024/12/13",
                    "Mid": "B454307F6CA03B56E0CFEC44EABF93BB67E56D6F",
                    "Name": "SangforVNC",
                    "PiracyRisk": 0,
                    "SoftwareId": 19054,
                    "Version": "7,1,0,2"
                },
                {
                    "CorpName": "",
                    "Id": 19053,
                    "InstallDate": "2024/08/27",
                    "Mid": "B454307F6CA03B56E0CFEC44EABF93BB67E56D6F",
                    "Name": "RayLink 8.1.0.9",
                    "PiracyRisk": 0,
                    "SoftwareId": 19053,
                    "Version": "8.1.0.9"
                },
                {
                    "CorpName": "",
                    "Id": 19052,
                    "InstallDate": "2024/12/17",
                    "Mid": "B454307F6CA03B56E0CFEC44EABF93BB67E56D6F",
                    "Name": "Python Launcher",
                    "PiracyRisk": 0,
                    "SoftwareId": 19052,
                    "Version": "3.13.1150.0"
                },
                {
                    "CorpName": "",
                    "Id": 19051,
                    "InstallDate": "2024/12/13",
                    "Mid": "B454307F6CA03B56E0CFEC44EABF93BB67E56D6F",
                    "Name": "Python 3.13.1 (64-bit)",
                    "PiracyRisk": 0,
                    "SoftwareId": 19051,
                    "Version": "3.13.1150.0"
                },
                {
                    "CorpName": "",
                    "Id": 19050,
                    "InstallDate": "2024/06/06",
                    "Mid": "B454307F6CA03B56E0CFEC44EABF93BB67E56D6F",
                    "Name": "Npcap 0.9982",
                    "PiracyRisk": 0,
                    "SoftwareId": 19050,
                    "Version": "0.9982"
                },
                {
                    "CorpName": "",
                    "Id": 19049,
                    "InstallDate": "2024/01/24",
                    "Mid": "B454307F6CA03B56E0CFEC44EABF93BB67E56D6F",
                    "Name": "Notepad++ (32-bit x86)",
                    "PiracyRisk": 0,
                    "SoftwareId": 19049,
                    "Version": "8.1.9"
                },
                {
                    "CorpName": "",
                    "Id": 18414,
                    "InstallDate": "2025/03/27",
                    "Mid": "B454307F6CA03B56E0CFEC44EABF93BB67E56D6F",
                    "Name": "NGNClient-TAP 1.1",
                    "PiracyRisk": 0,
                    "SoftwareId": 18414,
                    "Version": "1.1"
                },
                {
                    "CorpName": "",
                    "Id": 18411,
                    "InstallDate": "2025/03/28",
                    "Mid": "B454307F6CA03B56E0CFEC44EABF93BB67E56D6F",
                    "Name": "Mozilla Maintenance Service",
                    "PiracyRisk": 0,
                    "SoftwareId": 18411,
                    "Version": "136.0.1"
                },
                {
                    "CorpName": "",
                    "Id": 19048,
                    "InstallDate": "2024/03/14",
                    "Mid": "B454307F6CA03B56E0CFEC44EABF93BB67E56D6F",
                    "Name": "Microsoft Visual C++ 2015-2019 Redistributable (x64) - 14.28.29910",
                    "PiracyRisk": 0,
                    "SoftwareId": 19048,
                    "Version": "14.28.29910.0"
                },
                {
                    "CorpName": "",
                    "Id": 18949,
                    "InstallDate": "2024/06/06",
                    "Mid": "B454307F6CA03B56E0CFEC44EABF93BB67E56D6F",
                    "Name": "Microsoft Visual C++ 2013 Redistributable (x86) - 12.0.21005",
                    "PiracyRisk": 0,
                    "SoftwareId": 18949,
                    "Version": "12.0.21005.1"
                },
                {
                    "CorpName": "",
                    "Id": 22978,
                    "InstallDate": "2025/04/12",
                    "Mid": "B454307F6CA03B56E0CFEC44EABF93BB67E56D6F",
                    "Name": "Microsoft Edge WebView2 Runtime",
                    "PiracyRisk": 0,
                    "SoftwareId": 22978,
                    "Version": "135.0.3179.73"
                },
                {
                    "CorpName": "",
                    "Id": 19046,
                    "InstallDate": "2024/12/13",
                    "Mid": "B454307F6CA03B56E0CFEC44EABF93BB67E56D6F",
                    "Name": "EasyConnect",
                    "PiracyRisk": 0,
                    "SoftwareId": 19046,
                    "Version": "7,6,7,201"
                },
                {
                    "CorpName": "",
                    "Id": 19045,
                    "InstallDate": "2025/03/28",
                    "Mid": "B454307F6CA03B56E0CFEC44EABF93BB67E56D6F",
                    "Name": "DACS版本2023H1(43989)S",
                    "PiracyRisk": 0,
                    "SoftwareId": 19045,
                    "Version": "2023H1(43989)S"
                },
                {
                    "CorpName": "",
                    "Id": 18806,
                    "InstallDate": "2025/03/31",
                    "Mid": "B454307F6CA03B56E0CFEC44EABF93BB67E56D6F",
                    "Name": "Cloudbase-Init 1.1.2",
                    "PiracyRisk": 0,
                    "SoftwareId": 18806,
                    "Version": "1.1.2.0"
                },
                {
                    "CorpName": "",
                    "Id": 6786,
                    "InstallDate": "2024/01/30",
                    "Mid": "B454307F6CA03B56E0CFEC44EABF93BB67E56D6F",
                    "Name": "7-Zip 23.01 (x64)",
                    "PiracyRisk": 0,
                    "SoftwareId": 6786,
                    "Version": "23.01"
                }
            ],
            "Page": {
                "PageCount": 1,
                "PageNum": 1,
                "PageSize": 1000,
                "Total": 29
            }
        },
        "RequestId": "fc18a581-36b5-4904-90c0-a206583251d9"
    }
}
```

