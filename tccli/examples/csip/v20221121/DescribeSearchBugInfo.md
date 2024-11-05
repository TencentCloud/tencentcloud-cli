**Example 1: 查询漏洞信息**

查询应急漏洞信息

Input: 

```
tccli csip DescribeSearchBugInfo --cli-unfold-argument  \
    --Id 1
```

Output: 
```
{
    "Response": {
        "Data": {
            "CFWPatch": "1",
            "CWPFix": 0,
            "CWPScan": "0",
            "CveId": "CVE-2024-0884",
            "DataAsset": [
                {
                    "AppID": "12435623",
                    "CVEId": "CVE-2012-0023",
                    "IsScan": 1,
                    "InfluenceAsset": 45,
                    "NotRepairAsset": 33,
                    "NotProtectAsset": 24,
                    "TaskId": "mis-qbskll7i",
                    "TaskPercent": 100,
                    "TaskTime": "1630291892",
                    "ScanTime": "2022-1-12"
                }
            ],
            "DataBug": [
                {
                    "CVEId": "CVE-2023-22518",
                    "CVSSScore": "9.8",
                    "CreateTime": "2023-12-17T11:25:43+08:00",
                    "Fix": "1、目前官方已有可更新版本，建议受影响用户升级至如下对应固定版本：\nAtlassian Confluence >= 7.19.16\nAtlassian Confluence >= 8.3.4\nAtlassian Confluence >= 8.4.4\nAtlassian Confluence >= 8.5.3\nAtlassian Confluence >= 8.6.1\n参考链接：https://www.atlassian.com/software/confluence/download-archives\n2、缓解方案\t\n(1) 参考以下链接备份实例：https://confluence.atlassian.com/doc/production-backup-strategy-38797389.html；\n(2) 设置ACL限制外部可访问IP；\n(3) 建议结合业务实际情况，酌情从互联网上删除实例，直到可以进行升级。",
                    "Id": 1012504,
                    "ImpactCOMPENT": "(atlassian) confluence",
                    "ImpactOs": "debian",
                    "ImpactVersion": "version<7.19.16,8.0.0<=version<8.3.4,8.4.0<=version<8.4.4,8.5.0<=version<8.5.3,8.6.0<=version<8.6.1",
                    "IsPublish": 1,
                    "Level": "extreme",
                    "PatchId": "pcmgr-452553",
                    "ProSupport": 0,
                    "Reference": "url",
                    "ReleaseTime": "2023-10-30 16:09:48",
                    "SubCategory": "权限提升",
                    "Tag": "NETWORK,POC,KNOWN_EXPLOITED,APP",
                    "UpdateTime": "2023-12-17T11:25:43+08:00",
                    "VULCategory": 54,
                    "VULDescribe": "Confluence 是由 Atlassian 开发的知识管理与协同软件，旨在帮助团队协作、共享信息和创建文档。Confluence Data Center/Server 受影响版本中存在身份验证不当漏洞，未经身份验证的攻击者可构造恶意的请求提升权限，进而命令执行等。",
                    "VULName": "Atlassian Confluence Data Center and  Server 权限绕过漏洞（CVE-2023-22518）"
                }
            ],
            "DataSupport": [
                {
                    "VSSScan": true,
                    "CWPScan": "1",
                    "CFWPatch": "1",
                    "WafPatch": 1,
                    "CWPFix": 1,
                    "CveId": "CVE-2024-1889"
                }
            ],
            "StateCode": "1",
            "VSSScan": true,
            "WafPatch": 1
        },
        "RequestId": "ea962c2c-4d97-4412-9e3b-db533b59592b",
        "ReturnCode": 0,
        "ReturnMsg": "Success"
    }
}
```

