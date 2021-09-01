**Example 1: 绑定一个安全组至多个负载均衡**



Input: 

```
tccli clb SetSecurityGroupForLoadbalancers --cli-unfold-argument  \
    --SecurityGroup sg-12345678 \
    --OperationType ADD \
    --LoadBalancerIds lb-0936o712 lb-tttt5555
```

Output: 
```
{
    "Response": {
        "RequestId": "00ca7fca-90f1-47fe-a724-5d7e96d04633"
    }
}
```

