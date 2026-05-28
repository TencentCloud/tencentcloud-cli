**Example 1: 创建七层转发策略**



Input: 

```
tccli ga2 CreateForwardingPolicy --cli-unfold-argument  \
    --GlobalAcceleratorId ga-80bzejka \
    --ListenerId lsr-nd3qmz7h \
    --Host www.aaa.com
```

Output: 
```
{
    "Response": {
        "RequestId": "8306a684-0b45-4933-b8b5-eeac953fa4fa",
        "TaskId": "9f4180a9-80e4-4e74-a5ea-df9fee4b0aef",
        "ForwardingPolicyId": "dm-3vfx7nnq"
    }
}
```

