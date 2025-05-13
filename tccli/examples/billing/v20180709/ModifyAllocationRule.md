**Example 1: 编辑公摊规则**



Input: 

```
tccli billing ModifyAllocationRule --cli-unfold-argument  \
    --Name test_allocation2 \
    --RuleDetail.Connectors and \
    --RuleDetail.Children.0.RuleKey businessCode \
    --RuleDetail.Children.0.Operator  \
    --RuleDetail.Children.0.RuleValue p_cvm \
    --RuleDetail.Children.1.RuleKey regionId \
    --RuleDetail.Children.1.Operator  \
    --RuleDetail.Children.1.RuleValue 9 \
    --RuleDetail.Children.2.Connectors and \
    --RuleDetail.Children.2.Children.0.RuleKey projectId \
    --RuleDetail.Children.2.Children.0.Operator  \
    --RuleDetail.Children.2.Children.0.RuleValue 1270522 \
    --Type 1 \
    --RatioDetail.0.Ratio 40 \
    --RatioDetail.0.NodeId 13 \
    --RatioDetail.1.Ratio 60 \
    --RatioDetail.1.NodeId 14 \
    --RuleId 24
```

Output: 
```
{
    "Response": {
        "RequestId": "297a49ab-623b-4b3f-bd3a-1309cae4f76b"
    }
}
```

**Example 2: 编辑公摊规则示例**



Input: 

```
tccli billing ModifyAllocationRule --cli-unfold-argument  \
    --Name test_allocation1 \
    --RuleDetail.Connectors and \
    --RuleDetail.Children.0.RuleKey businessCode \
    --RuleDetail.Children.0.Operator  \
    --RuleDetail.Children.0.RuleValue p_nat \
    --Type 2 \
    --RatioDetail.0.Ratio 50 \
    --RatioDetail.0.NodeId 13 \
    --RatioDetail.1.Ratio 50 \
    --RatioDetail.1.NodeId 14 \
    --RuleId 22
```

Output: 
```
{
    "Response": {
        "RequestId": "937c1611-0e37-4a9d-8e01-f4854937a555"
    }
}
```

