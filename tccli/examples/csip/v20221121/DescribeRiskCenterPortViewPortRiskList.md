**Example 1: 获取端口视角的端口风险列表**

获取端口视角的端口风险列表

Input: 

```
tccli csip DescribeRiskCenterPortViewPortRiskList --cli-unfold-argument  \
    --MemberId mem-68b8087a65268000 mem-tencent-522badef8ad96a4d \
    --Filter.Limit 1 \
    --Filter.Offset 0
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "AffectAssetCount": "2",
                "AppId": "188651",
                "Component": "web",
                "FirstTime": "2024-07-07 12:05:29",
                "From": "云安全中心",
                "Id": "13f3cf8c53147c4183e6910",
                "Index": "13f3cf8c847c4183e6910",
                "Level": "middle",
                "Nick": "蛋糕",
                "NoHandleCount": 1,
                "Port": 443,
                "Protocol": "tcp",
                "RecentTime": "2024-08-13 11:21:02",
                "Service": "https,unknown",
                "Suggestion": 1,
                "Uin": "10088646"
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
        "RequestId": "13ed0f9d-5052-431d-b789-75bdf1e390bc",
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
        "TotalCount": 3
    }
}
```

