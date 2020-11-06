**Example 1: 修改黑石负载均衡实例的基本配置信息**



Input: 

```
tccli bmlb ModifyLoadBalancer --cli-unfold-argument  \
    --LoadBalancerId lb-q7qoi8cr \
    --LoadBalancerName abcd \
    --DomainPrefix qqq
```

Output: 
```
{
    "Response": {
        "TaskId": 2385751,
        "RequestId": "9cb9bd13-3db5-4b76-84ab-34b4fae5ef4c"
    }
}
```

