**Example 1: 调用示例**



Input: 

```
tccli csip DescribeBaselineAggregatedPolicyList --cli-unfold-argument  \
    --MemberId mem-tencent-6*************29
```

Output: 
```
{
    "Response": {
        "List": [
            {
                "CategoryStatistic": [
                    {
                        "Category": {
                            "CheckAssetType": "HOST",
                            "Description": "检测账号是否存在空口令、默认口令、字典口令，并核查密码复杂度与有效期策略，防范暴力破解攻击",
                            "ID": 50,
                            "Name": "Linux系统弱口令检测"
                        },
                        "NotPassItemCount": 0,
                        "NotPassItemRiskLevelStatistic": [
                            {
                                "NotPassCount": 0,
                                "RiskLevel": "HIGH"
                            }
                        ],
                        "PassItemCount": 1,
                        "PassRate": 100
                    }
                ],
                "CheckAssetType": "HOST",
                "ConfItemCount": 18,
                "Description": "检测账号是否存在空口令、默认口令、字典口令，并核查密码复杂度与有效期策略，防范暴力破解攻击",
                "Name": "弱口令",
                "NotPassItemCount": 0,
                "NotPassItemRiskLevelStatistic": [
                    {
                        "NotPassCount": 0,
                        "RiskLevel": "HIGH"
                    }
                ],
                "ParentCategoryID": 4,
                "PassItemCount": 5,
                "PassRate": 100,
                "PolicyID": [
                    761
                ],
                "PolicyType": "SYSTEM"
            }
        ],
        "RequestId": "7a28e0d4-9fbf-4d8a-9e2c-5d794067efbd"
    }
}
```

