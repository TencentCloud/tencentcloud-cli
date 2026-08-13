**Example 1: DescribeAILinkSetting**



Input: 

```
tccli csip DescribeAILinkSetting --cli-unfold-argument  \
    --MemberId mem-tencent-6f5795752f66e429
```

Output: 
```
{
    "Response": {
        "AILinkEnable": 1,
        "AutoInclude": 0,
        "ClusterIDs": [
            "cls-qyfsaqym"
        ],
        "ExcludeClusterIDs": [
            "0e***************************5e9"
        ],
        "ExcludeInstanceIds": [
            "ins-******ks"
        ],
        "InstanceIds": [
            "ins-******ks"
        ],
        "RuleScopeBalanced": 0,
        "RuleScopeDeep": 1,
        "RuleScopePrecise": 0,
        "Scope": 0,
        "TCSSScope": 0,
        "TagIDs": [],
        "RequestId": "bd5f3fcd-ad3e-47b8-b98a-8c90347307ca",
        "Quuids": [
            "66*******************************89d"
        ],
        "ExcludeQuuids": [
            "36*******************************453"
        ]
    }
}
```

