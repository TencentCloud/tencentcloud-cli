**Example 1: 开通外网实例**



Input: 

```
tccli redis AllocateWanAddress --cli-unfold-argument  \
    --InstanceId crs-5qlrlhux
```

Output: 
```
{
    "Response": {
        "FlowId": 327,
        "WanStatus": "外网开通中",
        "RequestId": "e546784b-709c-401d-aba6-73037eb4e522"
    }
}
```

