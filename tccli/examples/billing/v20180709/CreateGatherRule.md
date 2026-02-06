**Example 1: 创建归集嵌套规则**



Input: 

```
tccli billing CreateGatherRule --cli-unfold-argument  \
    --Id 8 \
    --RuleList.RuleDetail.Connectors and \
    --RuleList.RuleDetail.Children.0.RuleKey businessCode \
    --RuleList.RuleDetail.Children.0.Operator in \
    --RuleList.RuleDetail.Children.0.RuleValue p_cvm p_nat \
    --RuleList.RuleDetail.Children.1.RuleKey regionId \
    --RuleList.RuleDetail.Children.1.Operator in \
    --RuleList.RuleDetail.Children.1.RuleValue 9 5 \
    --RuleList.RuleDetail.Children.2.Connectors and \
    --RuleList.RuleDetail.Children.2.Children.0.RuleKey projectId \
    --RuleList.RuleDetail.Children.2.Children.0.Operator not in \
    --RuleList.RuleDetail.Children.2.Children.0.RuleValue 1270522
```

Output: 
```
{
    "Response": {
        "Id": 24,
        "RequestId": "4c396774-36bc-4897-a03d-41a18357d63d"
    }
}
```

**Example 2: 创建归集规则**



Input: 

```
tccli billing CreateGatherRule --cli-unfold-argument  \
    --Id 6 \
    --RuleList.RuleDetail.Connectors and \
    --RuleList.RuleDetail.Children.0.RuleKey businessCode \
    --RuleList.RuleDetail.Children.0.Operator in \
    --RuleList.RuleDetail.Children.0.RuleValue p_cvm p_nat
```

Output: 
```
{
    "Response": {
        "Id": 23,
        "RequestId": "215ccaa8-3b2b-425c-b53b-375df0c491e6"
    }
}
```

