**Example 1: 获取集群事件**



Input: 

```
tccli dlc GetRayClusterEvent --cli-unfold-argument  \
    --Id raycluster-20260529142346-h56t \
    --Page 1 \
    --PageSize 10 \
    --StartTime 1780039439000 \
    --EndTime 1780039439000
```

Output: 
```
{
    "Response": {
        "Context": "",
        "Events": [],
        "ListOver": true,
        "RequestId": "b2ac470f-de1d-4923-8057-2e10ead5e932"
    }
}
```

