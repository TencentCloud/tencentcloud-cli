**Example 1: 获取漏洞VPR信息**



Input: 

```
tccli csip DescribeHostVulItemVPRInfo --cli-unfold-argument  \
    --MemberId mem-tencent-6f5795752f66e429 \
    --VulID 102837
```

Output: 
```
{
    "Response": {
        "Label": [
            {
                "Level": "CRITICAL",
                "Name": "应急漏洞",
                "Remark": "被人为标记为应急漏洞"
            }
        ],
        "VRPRatingInfo": {
            "Remark": "该漏洞优先级为【紧急】。触发强制规则：被标记为应急漏洞。主要判定依据：暂无已知利用信息；技术利用性待进一步确认；根据 CVSS 评分评估危害程度。建议 72 小时内修复。",
            "Result": "URGENT",
            "Stage": [
                {
                    "Result": "暂无已知利用信息",
                    "Stage": "威胁活跃度"
                }
            ]
        },
        "RequestId": "bcfe2512-b55d-4bf1-9e66-c3ccb4b46928"
    }
}
```

