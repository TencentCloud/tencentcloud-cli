**Example 1: 获取资产视角的漏洞风险列表**

获取资产视角的漏洞风险列表

Input: 

```
tccli csip DescribeAssetViewVulRiskList --cli-unfold-argument  \
    --Filter.Filters.0.Name RecentTime \
    --Filter.Filters.0.Values '2024-10-26 19:37:21' \
    --Filter.Filters.0.OperatorType 4 \
    --Filter.Filters.1.Name RecentTime \
    --Filter.Filters.1.Values '2024-11-01 19:37:21' \
    --Filter.Filters.1.OperatorType 5 \
    --Filter.Filters.2.Name Status \
    --Filter.Filters.2.Values 0 \
    --Filter.Filters.2.OperatorType 7 \
    --Filter.Limit 10 \
    --Filter.Offset 0 \
    --Filter.Order desc \
    --Filter.By RecentTime
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "AffectAsset": "182.254.145.158",
                "AppId": "1300448058",
                "AppName": "OpenSSH",
                "AppVersion": "v1.0.1",
                "CVE": "CVE-2020-15778",
                "CVSS": 0,
                "CWPVersion": 4,
                "Component": "OpenSSH",
                "EMGCVulType": 0,
                "FirstTime": "2023-09-26 16:34:50",
                "From": "云安全中心",
                "HandleTaskId": "id-cnojiv",
                "Index": "360bfa2c*****",
                "InstanceId": "ins-***",
                "InstanceName": "ins-NAT1",
                "InstanceType": "CVM",
                "InstanceUUID": "7bb60327-***-****-***",
                "Level": "high",
                "Nick": "声声乌龙",
                "PCMGRId": "pcmgr-n21ln34l",
                "POCId": "c808d8eb****",
                "Payload": "OpenSSH/7.4",
                "Port": "22",
                "RecentTime": "2023-09-27 11:49:10",
                "RiskId": "1498f23a***",
                "Status": 0,
                "TaskId": "task-2k1b3",
                "Uin": "2190941624916",
                "VULName": "OpenSSH 命令注入漏洞(CVE-2020-15778)",
                "VULType": "命令注入",
                "VULURL": "/vul/detail?id=360bfa2c*****"
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

