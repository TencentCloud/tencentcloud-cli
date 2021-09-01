**Example 1: 创建黑石负载均衡七层监听器**



Input: 

```
tccli bmlb CreateL7Listeners --cli-unfold-argument  \
    --LoadBalancerId lb-47gazeml \
    --ListenerSet.0.LoadBalancerPort 81 \
    --ListenerSet.0.Protocol http \
    --ListenerSet.0.ListenerName http81
```

Output: 
```
{
    "Response": {
        "ListenerIds": [
            "lbl-l6fzjsx5"
        ],
        "RequestId": "155fdd8f-21f2-4f76-9d72-0729cc2a0dc6"
    }
}
```

