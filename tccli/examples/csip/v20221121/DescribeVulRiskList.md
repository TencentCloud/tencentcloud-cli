**Example 1: 查询云边界分析-暴露路径下主机节点的漏洞列表**



Input: 

```
tccli csip DescribeVulRiskList --cli-unfold-argument  \
    --CloudAccountID 100010421111 \
    --Provider tencent
```

Output: 
```
{
    "Response": {
        "RequestId": "8df95ddb-cc28-489d-a37d-422e0d93fe4b",
        "TotalCount": 882,
        "VulRiskList": [
            {
                "AssetID": "ins-xxxx",
                "CloudAccountID": "100010421111",
                "ContainerID": "",
                "CreateTime": "2025-05-15 01:18:44",
                "CveID": "CVE-2025-32911",
                "Description": "libsoup是GNOME项目的一款GNOME的HTTP客户端/服务器库。 libsoup存在安全漏洞，该漏洞源于函数soup_message_headers_get_content_disposition存在双重释放问题。",
                "Fix": "软件: libsoup2.4-1, 版本: 2.70.0-1\n\n修复命令\nsudo apt-get -y install libsoup2.4-1 --only-upgrade\n",
                "InstanceName": "测试平台",
                "InstanceStatus": "active",
                "UpdateTime": "2025-05-21 01:22:30",
                "VulCategory": "4",
                "VulCategoryName": "Linux软件漏洞",
                "VulLevel": "4",
                "VulLevelName": "严重",
                "VulName": "libsoup 安全漏洞(CVE-2025-32911)",
                "InstanceStatusName": "运行中"
            }
        ]
    }
}
```

