**Example 1: 合规管理检查项详情**



Input: 

```
tccli ssa DescribeComplianceDetail --cli-unfold-argument  \
    --Id 01034
```

Output: 
```
{
    "Response": {
        "CheckConfigDetail": {
            "Id": "7760c206-9655-11ea-89eb-6c92bf621820",
            "UUID": "6d269c6f-37d3-426e-8f4e-6fe06f6a9f31",
            "Category": "云计算安全扩展要求",
            "Type": "安全计算环境",
            "ErrorCount": 0,
            "NameEn": "check_cbs_autosnapshot",
            "SafeCount": 1,
            "IgnoreCount": 19,
            "RiskCount": 123,
            "ResCount": 143,
            "CheckName": "CBS-定期快照",
            "Method": "进入腾讯云“控制台-云服务器-云硬盘”，在云硬盘列表中找到相应的云硬盘，点击右方更多，选择设置数据定期快照策略，进行配置；并在“控制台-云服务器-快照-定期快照策略”中，查看对应快照策略是否处于开启状态。",
            "Doc": "https://cloud.tencent.com/document/product/362/8191",
            "AssetType": "cbs",
            "Content": "等保2.0中8.2.4.6要求云存储数据具备多个副本及数据恢复的功能。云硬盘的自动定期快照的功能，可以提供数据的备份和迁移能力。",
            "IsPass": 2,
            "LastCheckTime": "2020-08-05 01:36:49",
            "StandardItem": "数据备份恢复",
            "Chapter": "8.2.4.6",
            "AssetTypeDesc": "CBS",
            "IsIgnore": 0,
            "RiskItem": "CBS快照",
            "Title": "CBS-定期快照：云计算安全扩展要求-安全计算环境-数据备份恢复（8.2.4.6）"
        },
        "RequestId": "70442e41-d391-4226-aef0-659360c8e9df"
    }
}
```

