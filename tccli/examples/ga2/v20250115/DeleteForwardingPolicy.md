**Example 1: 删除七层转发策略**



Input: 

```
tccli ga2 DeleteForwardingPolicy --cli-unfold-argument  \
    --GlobalAcceleratorId ga-80bzejka \
    --ListenerId lsr-nd3qmz7h \
    --ForwardingPolicyId dm-io46vpu6
```

Output: 
```
{
    "Response": {
        "RequestId": "78864282-9abc-4f11-88e2-6548366b13f4",
        "TaskId": "0965b82a-5ed1-4d0a-b44c-70295a8fdad3"
    }
}
```

