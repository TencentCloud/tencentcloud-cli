**Example 1: 购买负载均衡实例**



Input: 

```
tccli ecm SetSecurityGroupForLoadbalancers --cli-unfold-argument  \
    --LoadBalancerIds lb-mov2697v \
    --SecurityGroup esg-0t3h9lmk \
    --OperationType ADD
```

Output: 
```
{
    "Response": {
        "RequestId": "88487432-ee86-4e5d-861b-774374121234"
    }
}
```

