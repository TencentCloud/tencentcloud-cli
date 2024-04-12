**Example 1: success1**

success1

Input: 

```
tccli csip DescribeAssetViewVulRiskList --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "AffectAsset": "182.254.145.158",
                "AppId": "1300448058",
                "AppName": "OpenSSH",
                "AppVersion": "-",
                "CVE": "CVE-2020-15778",
                "CVSS": 0,
                "CWPVersion": 4,
                "Component": "OpenSSH",
                "EMGCVulType": 0,
                "FirstTime": "2023-09-26 16:34:50",
                "From": "云安全中心",
                "HandleTaskId": "",
                "Index": "360bfa2cxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
                "InstanceId": "ins-xxx",
                "InstanceName": "[autotest][勿删]自动化测试NAT1",
                "InstanceType": "CVM",
                "InstanceUUID": "7bb60327-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
                "Level": "high",
                "Nick": "",
                "PCMGRId": "",
                "POCId": "c808d8ebxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
                "Payload": "OpenSSH/7.4",
                "Port": "22",
                "RecentTime": "2023-09-27 11:49:10",
                "RiskId": "1498f23axxxxxxxxxxxxxxxxxxxxxxxxxxx",
                "Status": 0,
                "TaskId": "",
                "Uin": "",
                "VULName": "OpenSSH 命令注入漏洞(CVE-2020-15778)",
                "VULType": "命令注入",
                "VULURL": ""
            }
        ],
        "FromLists": [
            {
                "Text": "云安全中心",
                "Value": "0"
            },
            {
                "Text": "主机检测",
                "Value": "1"
            },
            {
                "Text": "容器检测",
                "Value": "5"
            }
        ],
        "InstanceTypeLists": [
            {
                "Text": "CVM",
                "Value": "CVM"
            }
        ],
        "LevelLists": [
            {
                "Text": "严重",
                "Value": "extreme"
            },
            {
                "Text": "高危",
                "Value": "high"
            },
            {
                "Text": "中危",
                "Value": "middle"
            },
            {
                "Text": "低危",
                "Value": "low"
            },
            {
                "Text": "提示",
                "Value": "info"
            }
        ],
        "RequestId": "3c68de67-9f7e-442d-b1f0-81191bd1026e",
        "StatusLists": [
            {
                "Text": "未处理",
                "Value": "0"
            },
            {
                "Text": "标记已处置",
                "Value": "1"
            },
            {
                "Text": "已忽略",
                "Value": "2"
            },
            {
                "Text": "已修复",
                "Value": "3"
            }
        ],
        "Tags": [
            {
                "Text": "该漏洞存在在野利用或在野攻击",
                "Value": "KNOWN_EXPLOITED"
            },
            {
                "Text": "该漏洞仅能本地利用",
                "Value": "LOCAL"
            },
            {
                "Text": "该漏洞可作为系统组件漏洞检出",
                "Value": "SYS"
            },
            {
                "Text": "该漏洞可作为应用组件漏洞检出",
                "Value": "APP"
            },
            {
                "Text": "应急",
                "Value": "IS_EMERGENCY"
            },
            {
                "Text": "该漏洞可以远程利用",
                "Value": "NETWORK"
            },
            {
                "Text": "该漏洞有poc",
                "Value": "POC"
            },
            {
                "Text": "必修",
                "Value": "IS_SUGGEST"
            },
            {
                "Text": "该漏洞有exp",
                "Value": "EXP"
            }
        ],
        "TotalCount": 1102,
        "VULTypeLists": [
            {
                "Text": "处理逻辑错误",
                "Value": "处理逻辑错误"
            }
        ]
    }
}
```

