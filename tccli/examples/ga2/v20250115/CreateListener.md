**Example 1: 创建监听器**



Input: 

```
tccli ga2 CreateListener --cli-unfold-argument  \
    --GlobalAcceleratorId ga-80bzejka \
    --Name garendu-UDP \
    --PortRanges.FromPort 12 \
    --PortRanges.ToPort 12 \
    --Description garendu-UDP-desc \
    --ListenerType Standard \
    --IdleTimeout 13 \
    --GetRealIpType TOA \
    --ClientAffinity Open
```

Output: 
```
{
    "Response": {
        "ListenerId": "lsr-5lkfom8v",
        "RequestId": "3ca6812c-4782-4ca8-8ef7-e3753ab8a4c7",
        "TaskId": "85233b38-72cf-49ef-b3e8-c63ac9be774c"
    }
}
```

