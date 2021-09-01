**Example 1: 删除黑石负载均衡七层转发域名**



Input: 

```
tccli bmlb DeleteL7Domains --cli-unfold-argument  \
    --LoadBalancerId lb-47gazeml \
    --ListenerId lbl-l6fzjsx5 \
    --DomainIds dm-hg8j52ud
```

Output: 
```
{
    "Response": {
        "TaskId": 2385740,
        "RequestId": "2232b95e-fa18-4ca8-94f3-f008e74cb3b7"
    }
}
```

