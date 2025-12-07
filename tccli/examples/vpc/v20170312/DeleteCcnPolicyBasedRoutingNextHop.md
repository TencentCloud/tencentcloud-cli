**Example 1: 删除云联网策略路由下一跳**



Input: 

```
tccli vpc DeleteCcnPolicyBasedRoutingNextHop --cli-unfold-argument  \
    --CcnId ccn-7bw2xi31 \
    --PolicyBasedRoutingNextHopIds pbrnh-bbjdqarl
```

Output: 
```
{
    "Response": {
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

