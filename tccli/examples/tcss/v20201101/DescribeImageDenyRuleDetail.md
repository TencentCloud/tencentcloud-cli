**Example 1: 查询镜像拦截规则详情**



Input: 

```
tccli tcss DescribeImageDenyRuleDetail --cli-unfold-argument  \
    --RuleID xx
```

Output: 
```
{
    "Response": {
        "VulLabelSet": [
            "xx"
        ],
        "EffectImageSet": [
            "xx"
        ],
        "OperationUin": "xx",
        "EffectImageCount": 1,
        "ComponentSet": [
            "xx"
        ],
        "EffectStatus": "xx",
        "Status": 0,
        "EffectTime": "xx",
        "Risk": 1,
        "RiskLevelSet": [
            "xx"
        ],
        "RuleDescription": "xx",
        "Virus": 0,
        "VulLevelSet": [
            "xx"
        ],
        "PrivilegeDetail": [],
        "IsEffectAllImage": 0,
        "VirusMD5Set": [
            "xx"
        ],
        "RiskType": [
            "xx"
        ],
        "VirusName": [
            "xx"
        ],
        "RuleID": "xx",
        "Vul": 0,
        "UpdateTime": "xx",
        "RequestId": "xx",
        "CVEIDSet": [
            "xx"
        ],
        "ID": 1,
        "PrivilegeRun": 0,
        "VulClassSet": [
            "xx"
        ],
        "VirusLevelSet": [
            "xx"
        ],
        "RuleType": "xx",
        "RuleName": "xx",
        "EffectDay": 1
    }
}
```

