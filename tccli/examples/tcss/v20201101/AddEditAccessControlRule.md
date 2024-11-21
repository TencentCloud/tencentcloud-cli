**Example 1: 添加规则**



Input: 

```
tccli tcss AddEditAccessControlRule --cli-unfold-argument  \
    --RuleInfo.IsEnable True \
    --RuleInfo.RuleName llzlu_test \
    --RuleInfo.ImageIds sha256:eeb6ee3f44bd0b5103bb561b4c16bcb82328cfe5809ab675bb17ab3a16c517c9 sha256:2237821772abe2ea18714288644d774d33ea36b2017366da25f3d308c08fdea4 \
    --RuleInfo.RuleId 66f90eec43f38f311f8e22cf \
    --RuleInfo.ChildRules.0.ProcessPath */vi \
    --RuleInfo.ChildRules.0.RuleId 66f90eec43f38f311f8e22d0 \
    --RuleInfo.ChildRules.0.RuleMode RULE_MODE_ALERT \
    --RuleInfo.ChildRules.0.TargetFilePath /home/yunjing_testing_x86/*
```

Output: 
```
{
    "Response": {
        "RequestId": "fee1bdb0-c13f-4c65-b567-8e270df211c1"
    }
}
```

