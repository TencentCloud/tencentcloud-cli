**Example 1: 创建公摊规则1**



Input: 

```
tccli billing CreateAllocationRule --cli-unfold-argument  \
    --RuleList.Name 测试1 \
    --RuleList.Type 2 \
    --RuleList.RatioDetail.0.Ratio 25 \
    --RuleList.RatioDetail.0.NodeId 39926927 \
    --RuleList.RatioDetail.1.Ratio 25 \
    --RuleList.RatioDetail.1.NodeId 39926928 \
    --RuleList.RatioDetail.2.Ratio 25 \
    --RuleList.RatioDetail.2.NodeId 39926929 \
    --RuleList.RatioDetail.3.Ratio 25 \
    --RuleList.RatioDetail.3.NodeId 39926930 \
    --RuleList.RuleDetail.Connectors and \
    --RuleList.RuleDetail.Children.0.RuleKey ownerUin \
    --RuleList.RuleDetail.Children.0.Operator in \
    --RuleList.RuleDetail.Children.0.RuleValue 700000384179 \
    --RuleList.RuleDetail.Children.1.RuleKey businessCode \
    --RuleList.RuleDetail.Children.1.Operator in \
    --RuleList.RuleDetail.Children.1.RuleValue p_cbs \
    --RuleList.RuleDetail.Children.2.Connectors or \
    --RuleList.RuleDetail.Children.2.Children.0.RuleKey itemCode \
    --RuleList.RuleDetail.Children.2.Children.0.Operator in \
    --RuleList.RuleDetail.Children.2.Children.0.RuleValue sv_cbs_memspace_premium sv_cdn_cn_flux_package sv_ci_pkg_co_re_10 \
    --RuleList.RuleDetail.Children.3.RuleKey projectId \
    --RuleList.RuleDetail.Children.3.Operator in \
    --RuleList.RuleDetail.Children.3.RuleValue 0
```

Output: 
```
{
    "Response": {
        "Id": 287620,
        "RequestId": "71ff6535-bbbd-41f9-8b88-24395a59ef7b"
    }
}
```

