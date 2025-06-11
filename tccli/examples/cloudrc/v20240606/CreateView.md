**Example 1: 创建视图**



Input: 

```
tccli cloudrc CreateView --cli-unfold-argument  \
    --ViewName 测试视图 \
    --ConditionRule.Type complex \
    --ConditionRule.ComplexOption and \
    --ConditionRule.ComplexArray.0.Type complex \
    --ConditionRule.ComplexArray.0.ComplexArray.0.Type simple \
    --ConditionRule.ComplexArray.0.ComplexArray.0.SimpleKey RegionId \
    --ConditionRule.ComplexArray.0.ComplexArray.0.SimpleOption equals \
    --ConditionRule.ComplexArray.0.ComplexArray.0.SimpleValue 4 \
    --ConditionRule.ComplexArray.0.ComplexArray.1.Type simple \
    --ConditionRule.ComplexArray.0.ComplexArray.1.SimpleKey ZoneId \
    --ConditionRule.ComplexArray.0.ComplexArray.1.SimpleOption equals \
    --ConditionRule.ComplexArray.0.ComplexArray.1.SimpleValue 100008 100007 \
    --ConditionRule.ComplexArray.0.ComplexOption or \
    --ConditionRule.ComplexArray.1.Type simple \
    --ConditionRule.ComplexArray.1.SimpleKey PayMode \
    --ConditionRule.ComplexArray.1.SimpleOption equals \
    --ConditionRule.ComplexArray.1.SimpleValue 0 \
    --Tags.0.Key 应用 \
    --Tags.0.Value 默认应用
```

Output: 
```
{
    "Response": {
        "RequestId": "8a738fce-96a9-41de-870c-fb8ddb3b0394"
    }
}
```

