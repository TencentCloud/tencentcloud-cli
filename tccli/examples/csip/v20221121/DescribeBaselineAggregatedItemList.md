**Example 1: 调用示例**



Input: 

```
tccli csip DescribeBaselineAggregatedItemList --cli-unfold-argument  \
    --PolicyID 761 \
    --ParentCategoryID 4 \
    --CheckAssetType HOST \
    --CategoryID 50 \
    --MemberId mem-tencent-6*************29 \
    --Limit 10 \
    --Offset 0 \
    --Order asc \
    --By id
```

Output: 
```
{
    "Response": {
        "CheckObjectEnum": [
            {
                "Key": "HOST",
                "Value": "主机"
            }
        ],
        "List": [
            {
                "Appid": [
                    200000000
                ],
                "Item": {
                    "AffectedVersionList": [],
                    "Category": {
                        "CheckAssetType": "HOST",
                        "Description": "检测账号是否存在空口令、默认口令、字典口令，并核查密码复杂度与有效期策略，防范暴力破解攻击",
                        "ID": 50,
                        "Name": "Linux系统弱口令检测"
                    },
                    "CheckObject": [
                        "HOST"
                    ],
                    "CustomItemID": 0,
                    "DefaultValueList": [],
                    "Description": "系统存在弱口令，可以轻易被猜解，黑客可以通过暴力破解等方式进行密码爆破，从而获取系统用户密码，进而获得系统权限，导致服务器上的文件和数据泄露或者被用作其他攻击用途。",
                    "FixSuggestion": "修改对应用户的密码为足够强度的密码。",
                    "ID": 8,
                    "IsCustomConf": false,
                    "Name": "Linux系统弱口令检测",
                    "ReferenceLink": "https://b*********************************************A4",
                    "RiskLevel": "HIGH",
                    "RuleID": 1100,
                    "SupportCustomValue": false,
                    "SupportFix": true,
                    "SystemCategory": {
                        "CheckAssetType": "HOST",
                        "Description": "检测账号是否存在空口令、默认口令、字典口令，并核查密码复杂度与有效期策略，防范暴力破解攻击",
                        "ID": 4,
                        "Name": "弱口令"
                    },
                    "WebEditParam": ""
                },
                "JobID": [],
                "LatestCheckTime": "2026-08-11T12:51:15Z",
                "NotPassAssetCount": 0,
                "PassAssetCount": 11,
                "PassRate": 100,
                "ResultStatus": "PASS"
            }
        ],
        "TotalCount": 1,
        "RequestId": "0f45b1ef-7236-49b9-a2de-c0e87d8f742e"
    }
}
```

