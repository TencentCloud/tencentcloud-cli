**Example 1: 启停负载均衡实例**

启停负载均衡实例

Input: 

```
tccli clb SetLoadBalancerStartStatus --cli-unfold-argument  \
    --LoadBalancerId lb-xxxxxxxx \
    --OperationType Stop
```

Output: 
```
{
    "Response": {
        "RequestId": "abc"
    }
}
```

