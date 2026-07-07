**Example 1: 修改转发规则属性**



Input: 

```
tccli alb ModifyRulesAttributes --cli-unfold-argument  \
    --ListenerId lst-d9p3k7wa \
    --LoadBalancerId alb-f8q2xk9m \
    --Rules.0.Actions.0.FixedResponseConfig.Content OK \
    --Rules.0.Actions.0.FixedResponseConfig.ContentType text/html \
    --Rules.0.Actions.0.FixedResponseConfig.HttpCode 200 \
    --Rules.0.Actions.0.InsertHeaderConfig.Key ClientVer \
    --Rules.0.Actions.0.InsertHeaderConfig.Value 1.0 \
    --Rules.0.Actions.0.InsertHeaderConfig.ValueType UserDefined \
    --Rules.0.Actions.0.Order 1 \
    --Rules.0.Actions.0.RedirectConfig.Host www.redirect.com \
    --Rules.0.Actions.0.RedirectConfig.HttpCode 301 \
    --Rules.0.Actions.0.RedirectConfig.Path /redirecturl \
    --Rules.0.Actions.0.RedirectConfig.Port 443 \
    --Rules.0.Actions.0.RedirectConfig.Protocol HTTPS \
    --Rules.0.Actions.0.RedirectConfig.Query ${query} \
    --Rules.0.Actions.0.RemoveHeaderConfig.Key ClientVer \
    --Rules.0.Actions.0.RewriteConfig.Host www.myhost.com \
    --Rules.0.Actions.0.RewriteConfig.Path /redirecturl \
    --Rules.0.Actions.0.RewriteConfig.Query ${query} \
    --Rules.0.Actions.0.TargetGroupConfig.TargetGroupStickySession.Enabled False \
    --Rules.0.Actions.0.TargetGroupConfig.TargetGroupStickySession.Timeout 1000 \
    --Rules.0.Actions.0.TargetGroupConfig.TargetGroups.0.TargetGroupId lbtg-0zrnc9qa \
    --Rules.0.Actions.0.TargetGroupConfig.TargetGroups.0.Weight 10 \
    --Rules.0.Actions.0.Type TargetGroup \
    --Rules.0.Conditions.0.CookieConfig.0.Key ClientId \
    --Rules.0.Conditions.0.CookieConfig.0.Value xea4cd \
    --Rules.0.Conditions.0.HeaderConfig.Key ClientVer \
    --Rules.0.Conditions.0.HeaderConfig.Values 1.0 1.1 \
    --Rules.0.Conditions.0.HostConfig www.myhost.com \
    --Rules.0.Conditions.0.MethodConfig GET \
    --Rules.0.Conditions.0.PathConfig /url \
    --Rules.0.Conditions.0.QueryStringConfig.0.Key ClientVer \
    --Rules.0.Conditions.0.QueryStringConfig.0.Value 1.1 \
    --Rules.0.Conditions.0.SourceIpConfig 192.168.1.3/32 \
    --Rules.0.Conditions.0.Type Host \
    --Rules.0.Priority 100 \
    --Rules.0.RuleId rule-h8cy5gwl \
    --Rules.0.RuleName newName
```

Output: 
```
{
    "Response": {
        "RequestId": "3b848733-70e5-4558-ae39-4b9938eb7609"
    }
}
```

