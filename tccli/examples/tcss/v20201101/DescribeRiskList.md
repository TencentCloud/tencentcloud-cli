**Example 1: 查询集群风险项列表示例**



Input: 

```
tccli tcss DescribeRiskList --cli-unfold-argument  \
    --ClusterId cls-0zmsjvko \
    --Limit 2 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "RequestId": "ada3da6c-7aa9-48a7-9bdd-c9ae192fef65",
        "TotalCount": 18,
        "ClusterRiskItems": [
            {
                "CheckItem": {
                    "CheckItemId": 2,
                    "Name": "Apache containerd 安全漏洞",
                    "ItemDetail": "containerd是美国阿帕奇（Apache）基金会的一个容器守护进程。该进程根据RunCOCI规范负责控制宿主机上容器的完整周期。containerd1.3.9之前版本和1.4.3版本存在安全漏洞，该漏洞源于containerd-shimAPI被不正确地公开给主机网络容器。shimsAPI套接字的访问控制验证了连接进程的有效UID为0，但是没有限制对抽象Unix域套接字的访问。这将允许在与shim相同的网络名称空间中运行的恶意容器，其有效UID为0，但在其他方面减少了特权，从而导致使用elevat运行新进程。",
                    "RiskLevel": "Middle",
                    "RiskTarget": "Containerd",
                    "RiskType": "CVERisk",
                    "RiskAttribute": "PrivilegePromotion",
                    "RiskProperty": "ExistPOC ExistEXP ServerRestart",
                    "CVENumber": "CVE-2020-15257",
                    "DiscoverTime": "2020-12-01 11:15:00",
                    "Solution": "目前厂商已发布升级补丁以修复漏洞，补丁获取链接：https://github.com/containerd/containerd/commit/4a4bb851f5da563ff6e68a83dc837c7699c469ad",
                    "CVSS": "CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:C/C:L/I:L/A:N",
                    "CVSSScore": "5.2",
                    "RelateLink": "https://",
                    "AffectedType": "Node",
                    "AffectedVersion": "",
                    "IgnoredAssetNum": 0,
                    "IsIgnored": true,
                    "RiskAssessment": "test"
                },
                "VerifyInfo": "",
                "ErrorMessage": "",
                "AffectedClusterCount": 1,
                "AffectedNodeCount": 2
            }
        ]
    }
}
```

