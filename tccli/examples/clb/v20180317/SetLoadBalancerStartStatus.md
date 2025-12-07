**Example 1: 启停负载均衡实例**

启停负载均衡实例

Input: 

```
tccli clb SetLoadBalancerStartStatus --cli-unfold-argument  \
    --LoadBalancerId lb-hwdt33e0 \
    --OperationType Stop
```

Output: 
```
{
    "Response": {
        "RequestId": "b3196d4c-2722-4893-8d86-e33136199469"
    }
}
```

