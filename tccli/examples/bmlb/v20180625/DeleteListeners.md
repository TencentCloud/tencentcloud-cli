**Example 1: 删除黑石负载均衡监听器**



Input: 

```
tccli bmlb DeleteListeners --cli-unfold-argument  \
    --LoadBalancerId lb-47gazeml \
    --ListenerIds lbl-84j5v31f
```

Output: 
```
{
    "Response": {
        "TaskId": 2385734,
        "RequestId": "b082311a-f448-47be-af62-7944030e6ff1"
    }
}
```

