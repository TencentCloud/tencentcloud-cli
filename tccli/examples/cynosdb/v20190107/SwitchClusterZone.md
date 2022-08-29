**Example 1: 切换到从可用区**



Input: 

```
tccli cynosdb SwitchClusterZone --cli-unfold-argument  \
    --ClusterId xx \
    --OldZone xx \
    --NewZone xx \
    --IsInMaintainPeriod yes
```

Output: 
```
{
    "Response": {
        "FlowId": "123",
        "RequestId": "128046"
    }
}
```

