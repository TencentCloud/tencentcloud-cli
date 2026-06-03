**Example 1: 删除七层转发规则**



Input: 

```
tccli ga2 DeleteForwardingRule --cli-unfold-argument  \
    --GlobalAcceleratorId ga-n28np7la \
    --ListenerId lsr-n28osngd \
    --ForwardingPolicyId dm-80bzejra \
    --ForwardingRuleId rule-80osy9vy
```

Output: 
```
{
    "Response": {
        "RequestId": "23e8949a-487c-4c6a-82e9-fb1636eeac33",
        "TaskId": "eb498124-8195-429a-872a-7d33697efe4c"
    }
}
```

