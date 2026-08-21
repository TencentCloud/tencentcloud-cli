**Example 1: 调用示例**



Input: 

```
tccli csip DescribeBaselineFixRecordList --cli-unfold-argument  \
    --MemberId mem-tencent-6*************29 \
    --Limit 10 \
    --Offset 0 \
    --Order asc \
    --By ID
```

Output: 
```
{
    "Response": {
        "List": [
            {
                "AppID": 200000000,
                "AssetType": "HOST",
                "DiscoveryTime": "1970-01-01T00:00:00Z",
                "FixTime": "2026-07-15T08:36:09Z",
                "HostInfo": {
                    "AgentStatus": "ONLINE",
                    "Appid": 200000000,
                    "CloudTag": [],
                    "InstanceID": "lh**********o4",
                    "InstanceStatus": "RUNNING",
                    "Name": "漏洞二期测试lh-1",
                    "OsInfo": "Ubuntu Server 22.04 LTS 64bit",
                    "PrivateIP": "10.1.0.2",
                    "ProtectVersion": "ULTIMATE",
                    "PublicIP": "1.14.91.114",
                    "QUUID": "c*********************************8f",
                    "RegionInfo": {
                        "Region": "ap-guangzhou",
                        "RegionCode": "",
                        "RegionId": 0,
                        "RegionName": "广州",
                        "RegionNameEn": "Guangzhou"
                    },
                    "TagItem": [
                        {
                            "Color": "red",
                            "Description": "",
                            "ID": 123,
                            "TagKey": "csip",
                            "TagKeyEn": "csip",
                            "TagValue": "csip",
                            "TagValueEn": "csip"
                        }
                    ],
                    "UUID": "c*********************************8f"
                },
                "ID": 1,
                "ItemInfo": {
                    "AffectedVersionList": [],
                    "Category": {
                        "CheckAssetType": "HOST",
                        "Description": "等级保护2.0第二级安全要求，适用于一般性业务系统",
                        "ID": 144,
                        "Name": "等保二级-Ubuntu 22安全基线检查"
                    },
                    "CheckObject": [
                        "HOST"
                    ],
                    "CustomItemID": 0,
                    "DefaultValueList": [],
                    "Description": "配置审计日志文件的最大尺寸。一旦日志达到最大尺寸，它将被轮换，并开始一个新的日志文件。",
                    "FixSuggestion": "根据站点策略，在/etc/audit/auditd.conf中设置以下参数(<MB>需替换为具体的数字)：\nmax_log_file = <MB>。",
                    "ID": 3249,
                    "IsCustomConf": false,
                    "Name": "确保配置了审计日志存储大小",
                    "ReferenceLink": "",
                    "RiskLevel": "MEDIUM",
                    "RuleID": 11996,
                    "SupportCustomValue": false,
                    "SupportFix": false,
                    "SystemCategory": {
                        "CheckAssetType": "HOST",
                        "Description": "等级保护2.0第二级安全要求，适用于一般性业务系统",
                        "ID": 222,
                        "Name": "等保2.0二级"
                    },
                    "WebEditParam": ""
                }
            }
        ],
        "TotalCount": 4,
        "RequestId": "f3da60c4-5469-4dd5-baa4-7590ab0389c0"
    }
}
```

