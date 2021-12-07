**Example 1: 添加规则**



Input: 

```
tccli tcss AddEditAccessControlRule --cli-unfold-argument  \
    --RuleInfo.IsEnable true \
    --RuleInfo.ImageIds xxxx \
    --RuleInfo.ChildRules.0.RuleMode RULE_MODE_RELEASE \
    --RuleInfo.ChildRules.0.ProcessPath xxxx \
    --RuleInfo.ChildRules.0.TargetFilePath xxxx \
    --RuleInfo.RuleName xxxx
```

Output: 
```
{
    "Response": {
        "RequestId": "fee1bdb0-c13f-4c65-b567-8e270df211c1"
    }
}
```

**Example 2: 编辑规则**



Input: 

```
tccli tcss AddEditAccessControlRule --cli-unfold-argument  \
    --RuleInfo.IsEnable true \
    --RuleInfo.ImageIds xxxx \
    --RuleInfo.ChildRules.0.RuleMode RULE_MODE_RELEASE \
    --RuleInfo.ChildRules.0.ProcessPath xxxx \
    --RuleInfo.ChildRules.0.TargetFilePath xxxx \
    --RuleInfo.ChildRules.0.RuleId xxx \
    --RuleInfo.RuleName xxxx \
    --RuleInfo.RuleId 6038e07298dab13d32bc34ec
```

Output: 
```
{
    "Response": {
        "RequestId": "fee1bdb0-c13f-4c65-b567-8e270df211c1"
    }
}
```

