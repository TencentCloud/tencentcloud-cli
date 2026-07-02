**Example 1: DescribeAILinkSetting**

查询AI-Link智链引擎配置

Input: 

```
tccli csip DescribeAILinkSetting --cli-unfold-argument  \
    --MemberId mem-68************00
```

Output: 
```
{
    "Response": {
        "AILinkEnable": 1,
        "RuleScopeDeep": 1,
        "RuleScopeBalanced": 1,
        "RuleScopePrecise": 1,
        "Scope": 1,
        "Quuids": [
            "66******-****-****-****-**********9d"
        ],
        "ExcludeQuuids": [
            "36******-****-****-****-**********53"
        ],
        "AutoInclude": 1,
        "RequestId": "8c1f7156-fc01-4905-b286-e08f4db0eec2"
    }
}
```

