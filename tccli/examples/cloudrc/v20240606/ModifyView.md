**Example 1: 修改视图**



Input: 

```
tccli cloudrc ModifyView --cli-unfold-argument  \
    --ViewId vw-vr1yfbg7 \
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
    --ConditionRule.ComplexArray.1.SimpleValue 0
```

Output: 
```
{
    "Response": {
        "RequestId": "4d9ed385-e0cc-4733-bf5e-cd3f2669d3f7"
    }
}
```

