**Example 1: 替换VPC路由策略中的规则**

替换VPC路由策略中的规则。

Input: 

```
tccli vpc ReplaceRoutePolicyEntries --cli-unfold-argument  \
    --RoutePolicyId rrp-azd4dt1c \
    --RoutePolicyEntrySet.0.RoutePolicyEntryId rrpi-la0vk0g3 \
    --RoutePolicyEntrySet.0.Priority 1222
```

Output: 
```
{
    "Response": {
        "RequestId": "354f4ac3-8546-4516-8c8a-69e3ab73aa8a"
    }
}
```

