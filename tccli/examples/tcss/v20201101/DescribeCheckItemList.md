**Example 1: 查询所有检查项示例**



Input: 

```
tccli tcss DescribeCheckItemList --cli-unfold-argument  \
    --Limit 2 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "RequestId": "8d03392a-2a32-4950-b203-d2baf28057fe",
        "TotalCount": 34,
        "ClusterCheckItems": [
            {
                "CheckItemId": 1,
                "Name": "runc 安全漏洞",
                "ItemDetail": "runc是一款用于根据OCI规范生成和运行容器的CLI（命令行界面）工具。runc存在安全漏洞，攻击者可利用该漏洞将主机文件系统绑定到容器中。",
                "RiskLevel": "Serious",
                "RiskTarget": "runC",
                "RiskType": "CVERisk",
                "RiskAttribute": "PrivilegePromotion",
                "RiskProperty": "ExistPOC ExistEXP RemoteExploit ServerRestart",
                "CVENumber": "CVE-2021-30465",
                "DiscoverTime": "2021-05-27 21:15:00",
                "Solution": "目前厂商已发布升级补丁以修复漏洞，补丁获取链接：https://github.com/opencontainers/runc/security/advisories/GHSA-c3xm-pvg7-gh7r",
                "CVSS": "CVSS:3.1/AV:N/AC:H/PR:L/UI:N/S:C/C:H/I:H/A:H",
                "CVSSScore": "8.5",
                "RelateLink": "https://github.com/opencontainers/runc/security/advisories/GHSA-c3xm-pvg7-gh7r https://github.com/opencontainers/runc/releases http://www.openwall.com/lists/oss-security/2021/05/19/2",
                "AffectedType": "Node",
                "AffectedVersion": ""
            },
            {
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
                "RelateLink": "https://github.com/containerd/containerd/commit/4a4bb851f5da563ff6e68a83dc837c7699c469ad https://github.com/containerd/containerd/releases/tag/v1.4.3 https://github.com/containerd/containerd/security/advisories/GHSA-36xw-fx78-c5r4",
                "AffectedType": "Node",
                "AffectedVersion": ""
            }
        ]
    }
}
```

