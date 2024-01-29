**Example 1: 批量修改四层代理转发规则状态**

将 ZoneId 为 zone-24wjy25v1cwi 中 ProxyId 为 sid-2qwk27xf7j9g 中 RuleId 为 rule-2qzkbvx3hxl7 和 rule-3pszkbox0hm1 的规则全部停用。

Input: 

```
tccli teo ModifyL4ProxyRulesStatus --cli-unfold-argument  \
    --ZoneId zone-24wjy25v1cwi \
    --ProxyId sid-2qwk27xf7j9g \
    --RuleIds rule-2qzkbvx3hxl7 rule-3pszkbox0hm1 \
    --Status offline
```

Output: 
```
{
    "Response": {
        "RequestId": "6f8h5358-3159-4337-adc7-7604e01e0fa9"
    }
}
```

