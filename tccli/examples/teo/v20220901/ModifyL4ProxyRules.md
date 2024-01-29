**Example 1: 修改四层代理转发规则**

将 ZoneId 为 zone-24wjy25v1cwi 中 ProxyId 为 sid-2qwk27xf7j9g 中 RuleId 为 rule-2qzkbvx3hxl7 的规则的 RuleTag 调整为 service-1，Protocol 调整为 TCP，ClientIPPassThroughMode 调整为 TOA。

Input: 

```
tccli teo ModifyL4ProxyRules --cli-unfold-argument  \
    --ZoneId zone-24wjy25v1cwi \
    --ProxyId sid-2qwk27xf7j9g \
    --L4ProxyRules.0.RuleId rule-2qzkbvx3hxl7 \
    --L4ProxyRules.0.RuleTag service-1 \
    --L4ProxyRules.0.Protocol TCP \
    --L4ProxyRules.0.ClientIPPassThroughMode TOA
```

Output: 
```
{
    "Response": {
        "RequestId": "3df3e931-3119-4237-adc7-7604e01e0fa9"
    }
}
```

