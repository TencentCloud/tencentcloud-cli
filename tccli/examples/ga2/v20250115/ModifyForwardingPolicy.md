**Example 1: 修改七层转发策略**



Input: 

```
tccli ga2 ModifyForwardingPolicy --cli-unfold-argument  \
    --GlobalAcceleratorId ga-80bzejka \
    --ListenerId lsr-nd3qmz7h \
    --ForwardingPolicyId dm-io46vpu6 \
    --Host www.aaac.com
```

Output: 
```
{
    "Response": {
        "RequestId": "ca492969-ebcc-4b8c-994a-60c1dbad1844",
        "TaskId": "79ffdeef-b32f-49f1-9e1c-40d5c8750b4d"
    }
}
```

