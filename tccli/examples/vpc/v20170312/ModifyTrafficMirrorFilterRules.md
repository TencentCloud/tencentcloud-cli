**Example 1: 修改流量镜像过滤规则**



Input: 

```
tccli vpc ModifyTrafficMirrorFilterRules --cli-unfold-argument  \
    --TrafficMirrorId imgf-9ryixdn6 \
    --IngressFilterRules.0.Protocol UDP \
    --IngressFilterRules.0.TrafficMirrorFilterRuleId tmfi-7gk0gtdz
```

Output: 
```
{
    "Response": {
        "RequestId": "11797f58-1eb9-4d92-bd2e-dc467e3d5ccb"
    }
}
```

