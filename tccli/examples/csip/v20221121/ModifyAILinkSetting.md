**Example 1: ModifyAILinkSetting**



Input: 

```
tccli csip ModifyAILinkSetting --cli-unfold-argument  \
    --AILinkEnable 1 \
    --MemberId mem-tencent-6f5795752f66e429 \
    --RuleScopeDeep 1 \
    --RuleScopeBalanced 1 \
    --RuleScopePrecise 1 \
    --Scope 0 \
    --AutoInclude 0 \
    --TagIDs 1 \
    --TCSSScope 0 \
    --ClusterIDs 0e7**************************5e9 \
    --ExcludeClusterIDs 0e***************************5e9 \
    --InstanceIds ins-******ks \
    --ExcludeInstanceIds ins-*******s \
    --Quuids 36e*******************************53 \
    --ExcludeQuuids 36********************************53
```

Output: 
```
{
    "Response": {
        "RequestId": "b59ba586-ee91-4a49-a996-aa1b04c48313"
    }
}
```

