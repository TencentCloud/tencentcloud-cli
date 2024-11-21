**Example 1: 获取漏洞视角的漏洞风险列表**

获取漏洞视角的漏洞风险列表

Input: 

```
tccli csip DescribeVulViewVulRiskList --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "AffectAssetCount": 1,
                "AppId": "1300448058",
                "AppName": "app_andy",
                "AppVersion": "v1.0.0.1",
                "CVE": "CVE-2019-25032",
                "Component": "Unbound",
                "EMGCVulType": 0,
                "FirstTime": "2023-10-30 15:02:23",
                "From": "主机检测",
                "Index": "04c52dbf64c927a11b15840089e8f1d3",
                "Level": "high",
                "Nick": "andy",
                "NoHandleCount": 0,
                "PCMGRId": "pcmgr-n12on4o1n",
                "Payload": "bnd12iu41i",
                "Port": "621",
                "RecentTime": "2023-11-29 14:43:07",
                "RiskId": "04c52dbf64c927a11b15840089e8f1d3",
                "Uin": "1092741621",
                "VULName": "Unbound  输入验证错误漏洞 (CVE-2019-25032)",
                "VULType": "处理逻辑错误",
                "VULURL": "/hello/echo"
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
        "RequestId": "470926c1-52bf-46fb-bc00-be5d1b8cba9f",
        "Tags": [
            {
                "Text": "该漏洞有poc",
                "Value": "POC"
            },
            {
                "Text": "应急",
                "Value": "IS_EMERGENCY"
            },
            {
                "Text": "该漏洞可以远程利用",
                "Value": "NETWORK"
            }
        ],
        "TotalCount": 672,
        "VULTypeLists": [
            {
                "Text": "处理逻辑错误",
                "Value": "处理逻辑错误"
            }
        ]
    }
}
```

