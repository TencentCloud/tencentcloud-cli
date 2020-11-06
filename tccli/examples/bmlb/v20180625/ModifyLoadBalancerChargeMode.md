**Example 1: 更改黑石负载均衡的计费方式**



Input: 

```
tccli bmlb ModifyLoadBalancerChargeMode --cli-unfold-argument  \
    --LoadBalancerId lb-cegjj42t \
    --PayMode flow \
    --ListenerSet.0.ListenerId lbl-eluk9shx \
    --ListenerSet.0.Protocol http \
    --ListenerSet.0.Bandwidth 100
```

Output: 
```
{
    "Response": {
        "RequestId": "a9cc73ed-162e-444a-80e3-5a47a11f7689"
    }
}
```

