**Example 1: 编辑归集规则**



Input: 

```
tccli billing ModifyGatherRule --cli-unfold-argument  \
    --Id 23 \
    --RuleDetail.Connectors and \
    --RuleDetail.Children.0.RuleKey businessCode \
    --RuleDetail.Children.0.Operator not in \
    --RuleDetail.Children.0.RuleValue p_cvm p_nat
```

Output: 
```
{
    "Response": {
        "RequestId": "73c8c569-7791-4b2d-bc40-f3c18c5f40d2"
    }
}
```

**Example 2: 编辑归集规则1**



Input: 

```
tccli billing ModifyGatherRule --cli-unfold-argument  \
    --Id 24 \
    --RuleDetail.Connectors and \
    --RuleDetail.Children.0.RuleKey businessCode \
    --RuleDetail.Children.0.Operator in \
    --RuleDetail.Children.0.RuleValue p_cvm p_nat \
    --RuleDetail.Children.1.RuleKey regionId \
    --RuleDetail.Children.1.Operator in \
    --RuleDetail.Children.1.RuleValue 9 5 \
    --RuleDetail.Children.2.Connectors and \
    --RuleDetail.Children.2.Children.0.RuleKey projectId \
    --RuleDetail.Children.2.Children.0.Operator not in \
    --RuleDetail.Children.2.Children.0.RuleValue 1270522
```

Output: 
```
{
    "Response": {
        "RequestId": "901c2178-fa8d-4878-8680-952ea3788a59"
    }
}
```

