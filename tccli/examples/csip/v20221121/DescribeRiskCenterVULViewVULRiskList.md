**Example 1: 获取漏洞视角的漏洞风险列表**

获取漏洞视角的漏洞风险列表

Input: 

```
tccli csip DescribeRiskCenterVULViewVULRiskList --cli-unfold-argument  \
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
                "AffectAssetCount": 1,
                "AppId": "1315",
                "AppName": "perl",
                "AppVersion": "5.20.2-3+deb8u6",
                "CVE": "CVE-2017-12883",
                "Component": "perl",
                "Describe": "describe info",
                "EMGCVulType": 0,
                "FirstTime": "2024-09-12 14:50:06",
                "Fix": "升级到最新无漏洞版本\n建议您更新当前系统或软件至最新版，完成漏洞的修复。",
                "From": "容器检测",
                "Id": "0468eaa3505cf5ae9889a052",
                "Index": "0468ea5ae551fb98659a052",
                "Level": "extreme",
                "Nick": "声声乌龙",
                "NoHandleCount": 1,
                "Payload": "5.20.2-3+deb8u6",
                "Port": "80",
                "RecentTime": "2024-10-30 11:20:38",
                "References": "http://mirror.cucumberlinux.com/cucumber/cucumber-1.0/source/lang-base/perl/patches/CVE-2017-12883.patch",
                "Uin": "100178",
                "VULName": "PERL regular expression解析器缓冲区错误漏洞（CVE-2017-12883）",
                "VULType": "缓冲区溢出",
                "VULURL": "/usr/bin"
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
        "LevelLists": [
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
            },
            {
                "Text": "严重",
                "Value": "extreme"
            },
            {
                "Text": "高危",
                "Value": "high"
            }
        ],
        "RequestId": "848fbdea-ba54-4f46-aaaa-7f70f823b977",
        "TotalCount": 460,
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

