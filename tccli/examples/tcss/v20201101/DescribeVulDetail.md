**Example 1: 查询漏洞详情**



Input: 

```
tccli tcss DescribeVulDetail --cli-unfold-argument  \
    --PocID 1
```

Output: 
```
{
    "Response": {
        "RequestId": "2d770ee1-8360-4c62-badc-257688f1e4de",
        "VulInfo": {
            "CVEID": "CVE-2023-50164",
            "CVSSV3Desc": "CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H",
            "CVSSV3Score": 9.8,
            "Category": "OTHER",
            "CategoryType": "EMERGENCY",
            "ComponentList": [
                {
                    "FixedVersion": [
                        ">2.3.37",
                        "2.5.33",
                        "6.3.0.2"
                    ],
                    "Name": "(apache) struts",
                    "Version": [
                        "2.0.0<=version<=2.3.37",
                        "2.5.0<=version<2.5.33",
                        "6.0.0<=version<6.3.0.2"
                    ]
                }
            ],
            "ContainerCount": 0,
            "DefenceHostCount": 78,
            "DefenceScope": "ALL",
            "DefenceStatus": "DEFENDED",
            "DefendedCount": 0,
            "DefenseSolution": "官方已经发布了安全版本，建议受漏洞影响的用户立即更新Apache Struts2到最新安全版本。\n安全版本：\nApache Struts2 >= 2.5.33\nApache Struts2 >= 6.3.0.2\n官方下载地址：https://struts.apache.org/download.cgi 或修改项目依赖配置文件中的版本信息。",
            "Description": "Apache Struts2框架是一个用于开发Java EE网络应用程序的Web框架，它本质上相当于一个servlet，在MVC设计模式中，Struts2作为控制器(Controller)来建立模型与视图的数据交互。漏洞源于文件上传逻辑存在缺陷，攻击者可以操纵文件上传参数来启用路径遍历，在某些情况下，这可能导致上传可用于执行远程代码执行的恶意文件。",
            "Level": "CRITICAL",
            "LocalImageCount": 0,
            "LocalNewestImageCount": 0,
            "Name": "Apache Struts2 远程代码执行漏洞(CVE-2023-50164)",
            "OfficialSolution": "建议关注厂商公告或升级到最新版本。",
            "PocID": "pcmgr-5555555",
            "Reference": [
                "https://lists.apache.org/thread/yh09b3fkf6vz5d6jdgrlvmg60lfwtqhj"
            ],
            "RegistryImageCount": 0,
            "RegistryNewestImageCount": 0,
            "ScanStatus": "SCANNED",
            "SubmitTime": "2023-12-07 17:01:30",
            "Tags": [
                "NETWORK"
            ]
        }
    }
}
```

