**Example 1: 获取资产视角的弱口令风险列表**

获取资产视角的弱口令风险列表

Input: 

```
tccli csip DescribeRiskCenterAssetViewWeakPasswordRiskList --cli-unfold-argument  \
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
                "AffectAsset": "132.**.176.**",
                "AppId": "1302396215",
                "Component": "nginx",
                "FirstTime": "2024-10-28 06:05:21",
                "Fix": "修改对应用户的密码为足够强度的密码。",
                "From": "主机检测",
                "Id": "0bf10**a9d58***6ec5c7bfee04b",
                "Index": "cb07e221846d***4c42bb40***b0c37",
                "InstanceId": "ins-p7x4hn7p",
                "InstanceName": "cfw自动化",
                "InstanceType": "CVM",
                "Level": "high",
                "Nick": "声声乌龙",
                "PasswordType": "Linux系统弱口令检测",
                "Payload": "系统中存在弱口令: {\"hack\": \"pass******\"}",
                "RecentTime": "2024-10-30 06:03:26",
                "Service": "service",
                "Status": 0,
                "Uin": "100014592178",
                "VULType": "Linux系统弱口令检测",
                "VULURL": "http://url"
            }
        ],
        "FromLists": [
            {
                "Text": "主机检测",
                "Value": "1"
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
        "PasswordTypeLists": [
            {
                "Text": "Linux系统弱口令检测",
                "Value": "Linux系统弱口令检测"
            }
        ],
        "RequestId": "c1696722-47c5-48d5-919d-ecdba8414b23",
        "StatusLists": [
            {
                "Text": "未处理",
                "Value": "0"
            },
            {
                "Text": "已处置",
                "Value": "1"
            },
            {
                "Text": "已忽略",
                "Value": "2"
            },
            {
                "Text": "已封禁",
                "Value": "3"
            }
        ],
        "TotalCount": 1
    }
}
```

