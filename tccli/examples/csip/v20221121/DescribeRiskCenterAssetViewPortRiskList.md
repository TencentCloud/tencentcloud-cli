**Example 1: 获取资产视角的端口风险列表**

获取资产视角的端口风险列表

Input: 

```
tccli csip DescribeRiskCenterAssetViewPortRiskList --cli-unfold-argument  \
    --Filter.Limit 1
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "AffectAsset": "1.1.1.1",
                "AppId": "23445189",
                "Component": "OpenSSH",
                "FirstTime": "2024-04-19 16:14:02",
                "From": "云安全中心",
                "Id": "b6d76******",
                "Index": "1654******",
                "InstanceId": "ins-*****",
                "InstanceName": "cvm1",
                "InstanceType": "CVM",
                "Level": "middle",
                "Nick": "nickname",
                "Port": 22,
                "Protocol": "tcp",
                "RecentTime": "2024-06-07 14:22:58",
                "Service": "ssh",
                "Status": 3,
                "Suggestion": 1,
                "Uin": "22446133890"
            }
        ],
        "FromLists": [
            {
                "Text": "云安全中心",
                "Value": "0"
            },
            {
                "Text": "流量感知",
                "Value": "3"
            }
        ],
        "InstanceTypeLists": [
            {
                "Text": "CLB",
                "Value": "CLB"
            },
            {
                "Text": "CVM",
                "Value": "CVM"
            },
            {
                "Text": "EIP",
                "Value": "EIP"
            },
            {
                "Text": "VPN",
                "Value": "VPN"
            },
            {
                "Text": "NAT",
                "Value": "NAT"
            },
            {
                "Text": "OTHER",
                "Value": "OTHER"
            },
            {
                "Text": "LH",
                "Value": "LH"
            },
            {
                "Text": "HAVIP",
                "Value": "HAVIP"
            },
            {
                "Text": "NATFW",
                "Value": "NATFW"
            },
            {
                "Text": "未知",
                "Value": "unknown"
            },
            {
                "Text": "PROBE",
                "Value": "PROBE"
            },
            {
                "Text": "TSE",
                "Value": "TSE"
            },
            {
                "Text": "EC2",
                "Value": "EC2"
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
        "RequestId": "c95a495b-e2cb-4449-b101-1848c421aadd",
        "StatusLists": [
            {
                "Text": "已封禁",
                "Value": "3"
            },
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
            }
        ],
        "SuggestionLists": [
            {
                "Text": "保持现状",
                "Value": "0"
            },
            {
                "Text": "限制访问",
                "Value": "1"
            },
            {
                "Text": "封禁端口",
                "Value": "2"
            }
        ],
        "TotalCount": 42
    }
}
```

