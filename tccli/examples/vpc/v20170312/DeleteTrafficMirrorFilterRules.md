**Example 1: 删除流量镜像过滤规则**



Input: 

```
tccli vpc DeleteTrafficMirrorFilterRules --cli-unfold-argument  \
    --TrafficMirrorId imgf-9ryixdn6 \
    --EgressFilterRuleIds tmfi-bbc6a8cv
```

Output: 
```
{
    "Response": {
        "RequestId": "cdd38684-a9d2-4120-b39a-472bca1b9252"
    }
}
```

