**Example 1: 创建对等连接**



Input: 

```
tccli bmvpc CreateVpcPeerConnection --cli-unfold-argument  \
    --Version 2018-06-25 \
    --VpcId vpc-gapcv96p \
    --PeerVpcId vpc-ac09bc8y \
    --PeerRegion sh_bm \
    --VpcPeerConnectionName test-peer \
    --Bandwidth 1000
```

Output: 
```
{
    "Response": {
        "TaskId": 1234,
        "RequestId": "09186e64-d19e-4ca1-968f-df4fc8139192"
    }
}
```

