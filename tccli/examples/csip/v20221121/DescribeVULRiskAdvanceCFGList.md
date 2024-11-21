**Example 1: 查询漏洞风险高级配置**

查询漏洞风险高级配置

Input: 

```
tccli csip DescribeVULRiskAdvanceCFGList --cli-unfold-argument  \
    --MemberId mem-68b8087a65268000 \
    --Filter.Limit 1 \
    --Filter.Offset 0
```

Output: 
```
{
    "Response": {
        "CheckFromLists": [
            {
                "Text": "云安全中心",
                "Value": "0"
            },
            {
                "Text": "主机检测",
                "Value": "1"
            }
        ],
        "Data": [
            {
                "AttackHeat": "0",
                "CVE": "CVE-2024-45507",
                "CVSS": "9.8",
                "CheckFrom": "cpe",
                "EMGCVulType": 1,
                "Enable": 0,
                "FixMethod": [
                    "建议您更新当前系统或软件至最新版"
                ],
                "ImpactComponent": "(apache) ofbiz",
                "ImpactVersion": "version<18.12.16",
                "RecentScanTime": "2024-10-11 00:00:00",
                "References": "https://ofbiz.apache.org/download.html,https://ofbiz.apache.org/security.html,https://issues.apache.org/jira/browse/OFBIZ-13132,https://lists.apache.org/thread/o90dd9lbk1hh3t2557t2y2qvrh92p7wy",
                "ReleaseTime": "2024-09-04 17:15:00",
                "RiskId": "4c57121fa47a0d493ca934f6fa1bda31",
                "RiskLevel": "extreme",
                "ServiceSupport": [
                    {
                        "IsSupport": true,
                        "ServiceName": "cfw",
                        "SupportHandledCount": 0,
                        "SupportTotalCount": 0
                    },
                    {
                        "IsSupport": true,
                        "ServiceName": "cwp_detect",
                        "SupportHandledCount": 0,
                        "SupportTotalCount": 0
                    },
                    {
                        "IsSupport": true,
                        "ServiceName": "vss",
                        "SupportHandledCount": 0,
                        "SupportTotalCount": 0
                    }
                ],
                "VULDescribe": "Apache OFBiz是美国阿帕奇（Apache）基金会的一套企业资源计划（ERP）系统。该系统提供了一整套基于Java的Web应用程序组件和工具。 Apache OFBiz 18.12.16之前版本存在代码问题漏洞，该漏洞源于容易受到服务端请求伪造和代码注入攻击。",
                "VULName": "Apache OFBiz SSRF到远程代码执行漏洞（CVE-2024-45507）",
                "VULTag": [
                    "该漏洞可以远程利用",
                    "该漏洞有poc",
                    "该漏洞可作为应用组件漏洞检出"
                ],
                "VULType": "代码注入"
            }
        ],
        "RequestId": "b6826e70-03cf-4a5c-8796-1f943a5a76ab",
        "RiskLevelLists": [
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
            },
            {
                "Text": "中危",
                "Value": "middle"
            },
            {
                "Text": "低危",
                "Value": "low"
            }
        ],
        "TotalCount": 10,
        "VULTypeLists": [
            {
                "Text": "越界读取",
                "Value": "越界读取"
            },
            {
                "Text": "竞争条件",
                "Value": "竞争条件"
            },
            {
                "Text": "代码注入",
                "Value": "代码注入"
            },
            {
                "Text": "目录穿越 ",
                "Value": "目录穿越 "
            }
        ],
        "VulTagList": [
            {
                "Text": "该漏洞可以远程利用",
                "Value": "该漏洞可以远程利用"
            },
            {
                "Text": "该漏洞有exp",
                "Value": "该漏洞有exp"
            },
            {
                "Text": "该漏洞仅能本地利用",
                "Value": "该漏洞仅能本地利用"
            },
            {
                "Text": "该漏洞可作为系统组件漏洞检出",
                "Value": "该漏洞可作为系统组件漏洞检出"
            },
            {
                "Text": "该漏洞可作为应用组件漏洞检出",
                "Value": "该漏洞可作为应用组件漏洞检出"
            },
            {
                "Text": "应急",
                "Value": "应急"
            },
            {
                "Text": "必修",
                "Value": "必修"
            },
            {
                "Text": "该漏洞存在在野利用或在野攻击",
                "Value": "该漏洞存在在野利用或在野攻击"
            },
            {
                "Text": "该漏洞有poc",
                "Value": "该漏洞有poc"
            }
        ]
    }
}
```

