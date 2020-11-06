**Example 1: 删除黑石负载均衡七层转发规则**



Input: 

```
tccli bmlb DeleteL7Rules --cli-unfold-argument  \
    --LoadBalancerId lb-47gazeml \
    --ListenerId lbl-l6fzjsx5 \
    --DomainId dm-5ugypezt \
    --LocationIds loc-iu47kdm3
```

Output: 
```
{
    "Response": {
        "TaskId": 2385739,
        "RequestId": "3552d4f9-f95c-4f41-a69d-d073750bdf53"
    }
}
```

