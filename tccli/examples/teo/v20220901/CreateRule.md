**Example 1: CreateRule**

创建一个规则引擎

Input: 

```
tccli teo CreateRule --cli-unfold-argument  \
    --Status disable \
    --Rules.0.Actions.0.NormalAction.Action RangeOriginPull \
    --Rules.0.Actions.0.NormalAction.Parameters.0.Name Switch \
    --Rules.0.Actions.0.NormalAction.Parameters.0.Values on \
    --Rules.0.Actions.1.CodeAction.Action StatusCodeCache \
    --Rules.0.Actions.1.CodeAction.Parameters.0.Name CacheTime \
    --Rules.0.Actions.1.CodeAction.Parameters.0.StatusCode 200 \
    --Rules.0.Actions.1.CodeAction.Parameters.0.Values 20 \
    --Rules.0.Actions.2.RewriteAction.Action ResponseHeader \
    --Rules.0.Actions.2.RewriteAction.Parameters.0.Action set \
    --Rules.0.Actions.2.RewriteAction.Parameters.0.Name Foo \
    --Rules.0.Actions.2.RewriteAction.Parameters.0.Values Bar \
    --Rules.0.Actions.2.RewriteAction.Parameters.1.Action add \
    --Rules.0.Actions.2.RewriteAction.Parameters.1.Name Hello \
    --Rules.0.Actions.2.RewriteAction.Parameters.1.Values World \
    --Rules.0.Actions.2.RewriteAction.Parameters.2.Action del \
    --Rules.0.Actions.2.RewriteAction.Parameters.2.Name Foo2 \
    --Rules.0.Conditions.0.Conditions.0.Operator equal \
    --Rules.0.Conditions.0.Conditions.0.Target host \
    --Rules.0.Conditions.0.Conditions.0.Values test.vernayang.com \
    --RuleName new_rule01 \
    --ZoneId zone-qbjifysd
```

Output: 
```
{
    "Response": {
        "RequestId": "811d2583-310c-41f4-b5e7-abe4074047d4",
        "RuleId": "rule-djuqmq"
    }
}
```

**Example 2: 修改源站为IP域名**

规则引擎修改源站为IP域名

Input: 

```
tccli teo CreateRule --cli-unfold-argument  \
    --ZoneId zone-2kmrcz5heaw2 \
    --RuleName test_origin \
    --Status enable \
    --Rules.0.Conditions.0.Conditions.0.Operator equal \
    --Rules.0.Conditions.0.Conditions.0.Target host \
    --Rules.0.Conditions.0.Conditions.0.IgnoreCase False \
    --Rules.0.Conditions.0.Conditions.0.Values rule.test.cloud \
    --Rules.0.Conditions.0.Conditions.1.Operator equal \
    --Rules.0.Conditions.0.Conditions.1.Target client_country \
    --Rules.0.Conditions.0.Conditions.1.IgnoreCase False \
    --Rules.0.Conditions.0.Conditions.1.Values CN \
    --Rules.0.Actions.0.NormalAction.Action Origin \
    --Rules.0.Actions.0.NormalAction.Parameters.0.Name Type \
    --Rules.0.Actions.0.NormalAction.Parameters.0.Values IP_DOMAIN \
    --Rules.0.Actions.0.NormalAction.Parameters.1.Name DomainName \
    --Rules.0.Actions.0.NormalAction.Parameters.1.Values 1.1.1.1 \
    --Rules.0.Actions.0.NormalAction.Parameters.2.Name OriginProtocol \
    --Rules.0.Actions.0.NormalAction.Parameters.2.Values follow \
    --Rules.0.Actions.0.NormalAction.Parameters.3.Name HttpOriginPort \
    --Rules.0.Actions.0.NormalAction.Parameters.3.Values 80 \
    --Rules.0.Actions.0.NormalAction.Parameters.4.Name HttpsOriginPort \
    --Rules.0.Actions.0.NormalAction.Parameters.4.Values 443
```

Output: 
```
{
    "Response": {
        "RuleId": "rule-djuqsx",
        "RequestId": "811d2583-310c-41f4-b5e7-abe4074047d4"
    }
}
```

**Example 3: 修改源站为源站组**

规则引擎修改源站为源站组

Input: 

```
tccli teo CreateRule --cli-unfold-argument  \
    --ZoneId zone-2kmrcz5heaw2 \
    --RuleName test_origin \
    --Status enable \
    --Rules.0.Conditions.0.Conditions.0.Operator equal \
    --Rules.0.Conditions.0.Conditions.0.Target host \
    --Rules.0.Conditions.0.Conditions.0.IgnoreCase False \
    --Rules.0.Conditions.0.Conditions.0.Values rule.test.cloud \
    --Rules.0.Conditions.0.Conditions.1.Operator equal \
    --Rules.0.Conditions.0.Conditions.1.Target client_country \
    --Rules.0.Conditions.0.Conditions.1.IgnoreCase False \
    --Rules.0.Conditions.0.Conditions.1.Values CN \
    --Rules.0.Actions.0.NormalAction.Action Origin \
    --Rules.0.Actions.0.NormalAction.Parameters.0.Name Type \
    --Rules.0.Actions.0.NormalAction.Parameters.0.Values OriginGroup \
    --Rules.0.Actions.0.NormalAction.Parameters.1.Name OriginGroupId \
    --Rules.0.Actions.0.NormalAction.Parameters.1.Values origin-ff7e677b-2c4d-11ee-9687-525400521111 \
    --Rules.0.Actions.0.NormalAction.Parameters.2.Name OriginProtocol \
    --Rules.0.Actions.0.NormalAction.Parameters.2.Values follow \
    --Rules.0.Actions.0.NormalAction.Parameters.3.Name HttpOriginPort \
    --Rules.0.Actions.0.NormalAction.Parameters.3.Values 80 \
    --Rules.0.Actions.0.NormalAction.Parameters.4.Name HttpsOriginPort \
    --Rules.0.Actions.0.NormalAction.Parameters.4.Values 443
```

Output: 
```
{
    "Response": {
        "RuleId": "rule-djuq9s",
        "RequestId": "811d2583-310c-41f4-b5e7-abe407404sdsd"
    }
}
```

**Example 4: 修改源站为负载均衡**

规则引擎修改源站为负载均衡

Input: 

```
tccli teo CreateRule --cli-unfold-argument  \
    --ZoneId zone-2kmrcz5heaw2 \
    --RuleName test_origin \
    --Status enable \
    --Rules.0.Conditions.0.Conditions.0.Operator equal \
    --Rules.0.Conditions.0.Conditions.0.Target host \
    --Rules.0.Conditions.0.Conditions.0.IgnoreCase False \
    --Rules.0.Conditions.0.Conditions.0.Values rule.test.cloud \
    --Rules.0.Conditions.0.Conditions.1.Operator equal \
    --Rules.0.Conditions.0.Conditions.1.Target client_country \
    --Rules.0.Conditions.0.Conditions.1.IgnoreCase False \
    --Rules.0.Conditions.0.Conditions.1.Values CN \
    --Rules.0.Actions.0.NormalAction.Action Origin \
    --Rules.0.Actions.0.NormalAction.Parameters.0.Name Type \
    --Rules.0.Actions.0.NormalAction.Parameters.0.Values LoadBalance \
    --Rules.0.Actions.0.NormalAction.Parameters.1.Name OriginGroupId \
    --Rules.0.Actions.0.NormalAction.Parameters.1.Values lb-ff7e677b-2c4d-11ee-9687 \
    --Rules.0.Actions.0.NormalAction.Parameters.2.Name OriginProtocol \
    --Rules.0.Actions.0.NormalAction.Parameters.2.Values follow \
    --Rules.0.Actions.0.NormalAction.Parameters.3.Name HttpOriginPort \
    --Rules.0.Actions.0.NormalAction.Parameters.3.Values 80 \
    --Rules.0.Actions.0.NormalAction.Parameters.4.Name HttpsOriginPort \
    --Rules.0.Actions.0.NormalAction.Parameters.4.Values 443
```

Output: 
```
{
    "Response": {
        "RuleId": "rule-djuq91",
        "RequestId": "811d2583-310c-41f4-b5e7-abe407404xs"
    }
}
```

**Example 5: 修改源站为S3对象存储**

规则引擎修改源站为S3兼容的对象存储

Input: 

```
tccli teo CreateRule --cli-unfold-argument  \
    --ZoneId zone-2kmrcz5heaw2 \
    --RuleName test_origin \
    --Status enable \
    --Rules.0.Conditions.0.Conditions.0.Operator equal \
    --Rules.0.Conditions.0.Conditions.0.Target host \
    --Rules.0.Conditions.0.Conditions.0.IgnoreCase False \
    --Rules.0.Conditions.0.Conditions.0.Values rule.test.cloud \
    --Rules.0.Conditions.0.Conditions.1.Operator equal \
    --Rules.0.Conditions.0.Conditions.1.Target client_country \
    --Rules.0.Conditions.0.Conditions.1.IgnoreCase False \
    --Rules.0.Conditions.0.Conditions.1.Values CN \
    --Rules.0.Actions.0.NormalAction.Action Origin \
    --Rules.0.Actions.0.NormalAction.Parameters.0.Name Type \
    --Rules.0.Actions.0.NormalAction.Parameters.0.Values AWS_S3 \
    --Rules.0.Actions.0.NormalAction.Parameters.1.Name ServerName \
    --Rules.0.Actions.0.NormalAction.Parameters.1.Values bucke_name.gcp.storage.com \
    --Rules.0.Actions.0.NormalAction.Parameters.2.Name PrivateAccess \
    --Rules.0.Actions.0.NormalAction.Parameters.2.Values on \
    --Rules.0.Actions.0.NormalAction.Parameters.3.Name AccessKeyId \
    --Rules.0.Actions.0.NormalAction.Parameters.3.Values xxxx******xxxx \
    --Rules.0.Actions.0.NormalAction.Parameters.4.Name SecretAccessKey \
    --Rules.0.Actions.0.NormalAction.Parameters.4.Values xxxx******xxxx \
    --Rules.0.Actions.0.NormalAction.Parameters.5.Name SignatureVersion \
    --Rules.0.Actions.0.NormalAction.Parameters.5.Values v4 \
    --Rules.0.Actions.0.NormalAction.Parameters.6.Name Region \
    --Rules.0.Actions.0.NormalAction.Parameters.6.Values ap-guangzhou
```

Output: 
```
{
    "Response": {
        "RuleId": "rule-djuq23",
        "RequestId": "811d2583-310c-41f4-b5e7-abe407404sxsd"
    }
}
```

**Example 6: 修改源站为COS对象存储**

规则引擎修改源站为COS对象存储

Input: 

```
tccli teo CreateRule --cli-unfold-argument  \
    --ZoneId zone-2kmrcz5heaw2 \
    --RuleName test_origin \
    --Status enable \
    --Rules.0.Conditions.0.Conditions.0.Operator equal \
    --Rules.0.Conditions.0.Conditions.0.Target host \
    --Rules.0.Conditions.0.Conditions.0.IgnoreCase False \
    --Rules.0.Conditions.0.Conditions.0.Values rule.test.cloud \
    --Rules.0.Conditions.0.Conditions.1.Operator equal \
    --Rules.0.Conditions.0.Conditions.1.Target client_country \
    --Rules.0.Conditions.0.Conditions.1.IgnoreCase False \
    --Rules.0.Conditions.0.Conditions.1.Values CN \
    --Rules.0.Actions.0.NormalAction.Action Origin \
    --Rules.0.Actions.0.NormalAction.Parameters.0.Name Type \
    --Rules.0.Actions.0.NormalAction.Parameters.0.Values COS \
    --Rules.0.Actions.0.NormalAction.Parameters.1.Name ServerName \
    --Rules.0.Actions.0.NormalAction.Parameters.1.Values bucke_name.gcp.storage.com \
    --Rules.0.Actions.0.NormalAction.Parameters.2.Name CosPrivateAccess \
    --Rules.0.Actions.0.NormalAction.Parameters.2.Values on
```

Output: 
```
{
    "Response": {
        "RuleId": "rule-djuq21",
        "RequestId": "811d2583-310c-41f4-b5e7-abe407404hs"
    }
}
```

