**Example 1: 获取资产视角的漏洞风险列表**

获取资产视角的漏洞风险列表

Input: 

```
tccli csip DescribeRiskCenterAssetViewVULRiskList --cli-unfold-argument  \
    --MemberId mem-68b8087a65268000 \
    --Filter.Limit 1 \
    --Filter.Offset 0
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "AffectAsset": "ins-9527",
                "AppId": "1302111215",
                "AppName": "libcurl-minimal,curl",
                "AppVersion": "7.61.1-18.el8",
                "CVE": "CVE-2023-27536",
                "CWPVersion": 0,
                "Component": "curl,libcurl-minimal",
                "Describe": "describe info",
                "EMGCVulType": 0,
                "FirstTime": "2024-08-29 00:10:36",
                "Fix": "建议关注厂商公告或升级到最新版本。\n建议您更新当前系统或软件至最新版，完成漏洞的修复。",
                "From": "容器检测",
                "Id": "11fc83d411bad6***71e4f9ef862dc",
                "Index": "5f31127***99f4ae379c0880d43c285",
                "InstanceId": "sha256:5d***dc976460b***c8a1ad043720b***fc16c52c45d4847e53fadb6",
                "InstanceName": "centos",
                "InstanceType": "Local",
                "InstanceUUID": "3cbf2d8f-c40a-452a-92ec-140f9b2d29a2",
                "IsSupportDetect": false,
                "IsSupportRepair": false,
                "Level": "extreme",
                "Nick": "声声乌龙",
                "POCId": "pcmgr-407***",
                "Payload": "7.61.1-18.el8",
                "Port": "80",
                "RecentTime": "2024-10-30 11:20:39",
                "References": "https://hackerone.com/reports/1895135",
                "Service": "service",
                "Status": 0,
                "Uin": "10001122178",
                "VULName": "Curl 身份认证绕过漏洞(CVE-2023-27536)",
                "VULType": "其他",
                "VULURL": "http://url"
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
                "Text": "托管集群",
                "Value": "managed_cluster"
            },
            {
                "Text": "CVM",
                "Value": "CVM"
            },
            {
                "Text": "本地镜像",
                "Value": "Local"
            },
            {
                "Text": "CLB",
                "Value": "CLB"
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
        "RequestId": "efdf251a-7f1a-4b9b-8e61-a19fc018ffa9",
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
        "TotalCount": 532,
        "VULTypeLists": [
            {
                "Text": "信息泄漏",
                "Value": "信息泄漏"
            },
            {
                "Text": "处理逻辑错误",
                "Value": "处理逻辑错误"
            },
            {
                "Text": "其他",
                "Value": "其他"
            },
            {
                "Text": "路径遍历",
                "Value": "路径遍历"
            },
            {
                "Text": "授权问题",
                "Value": "授权问题"
            },
            {
                "Text": "注入漏洞",
                "Value": "注入漏洞"
            },
            {
                "Text": "代码注入",
                "Value": "代码注入"
            },
            {
                "Text": "缓冲区溢出",
                "Value": "缓冲区溢出"
            },
            {
                "Text": "配置错误",
                "Value": "配置错误"
            },
            {
                "Text": "加密问题",
                "Value": "加密问题"
            },
            {
                "Text": "跨站脚本",
                "Value": "跨站脚本"
            },
            {
                "Text": "命令注入",
                "Value": "命令注入"
            }
        ]
    }
}
```

