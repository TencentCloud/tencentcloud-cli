**Example 1: 查询云边界分析-暴露路径下主机节点的高危基线风险列表**



Input: 

```
tccli csip DescribeHighBaseLineRiskList --cli-unfold-argument  \
    --CloudAccountID 100014592178 \
    --Provider tencent
```

Output: 
```
{
    "Response": {
        "HighBaseLineRiskList": [
            {
                "AssetID": "ins-xxs13fd",
                "CloudAccountID": "123342644",
                "CreateTime": "2024-12-26 21:28:51",
                "FixAdvice": "",
                "InstanceName": "主机x安全中心(请勿删除)",
                "InstanceStatus": "active",
                "InstanceStatusName": "运行中",
                "RiskCategory": "4",
                "RiskCategoryName": "弱口令",
                "RiskDesc": "系统存在弱口令，可以轻易被猜解，黑客可以通过暴力破解等方式进行密码爆破，从而获取系统用户密码，进而获得系统权限，导致服务器上的文件和数据泄露或者被用作其他攻击用途。",
                "RiskLevel": "3",
                "RiskLevelName": "高危",
                "RiskName": "Linux系统弱口令检测",
                "RiskResult": "系统中存在弱口令: {\"testxxxx\": \"123******\"}",
                "UpdateTime": "2025-04-22 10:32:19"
            }
        ],
        "RequestId": "0a44ea12-dce32-46a13-8eb19-2ea7872bb96b",
        "TotalCount": 1
    }
}
```

