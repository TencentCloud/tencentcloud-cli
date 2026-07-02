**Example 1: ModifyAILinkSetting**

修改AI-Link智链引擎配置

Input: 

```
tccli csip ModifyAILinkSetting --cli-unfold-argument  \
    --AILinkEnable 1 \
    --RuleScopeDeep 1 \
    --RuleScopeBalanced 1 \
    --RuleScopePrecise 1 \
    --Scope 1 \
    --AutoInclude 1 \
    --MemberId mem-68************00 \
    --Quuids 66******-****-****-****-**********9d \
    --ExcludeQuuids 36******-****-****-****-**********53
```

Output: 
```
{
    "Response": {
        "RequestId": "95c9fd49-f547-4425-b67a-67bb99396e13"
    }
}
```

