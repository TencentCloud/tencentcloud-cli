**Example 1: 测试用例**



Input: 

```
tccli waf ModifyLLMContentRule --cli-unfold-argument  \
    --Domain jacky12220901.testwaf.com \
    --Name ddptest \
    --ActionType log \
    --Priority 50 \
    --Status 1 \
    --ResponseText ceshi \
    --CheckType 1 \
    --RuleItem.0.Key inappropriate_info \
    --RuleItem.0.Op contain \
    --RuleItem.0.Value 601 \
    --RuleItem.0.Levels.0.Label 601 \
    --RuleItem.0.Levels.0.Level 400 \
    --SessionApplied 0 \
    --Options.0.Key protectpath_business \
    --Options.0.Op belong \
    --Options.0.Value ` \
    --Options.0.Name 5300000310 \
    --InstanceId waf_2l15d14809yfq9sf \
    --ReplyType 1 \
    --CustomReplyRuleId 0
```

Output: 
```
{
    "Response": {
        "RuleId": "5200039233",
        "RequestId": "23a6c61f-825a-4a88-a03c-00a6859d1928"
    }
}
```

