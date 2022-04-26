**Example 1: 关闭外网实例**



Input: 

```
tccli redis ReleaseWanAddress --cli-unfold-argument  \
    --InstanceId crs-5qlrlhux
```

Output: 
```
{
    "Response": {
        "FlowId": 327,
        "WanStatus": "外网关闭中",
        "RequestId": "e546784b-709c-401d-aba6-73037eb4e522"
    }
}
```

