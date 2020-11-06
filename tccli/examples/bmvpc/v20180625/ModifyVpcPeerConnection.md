**Example 1: 修改黑石对等连接属性**



Input: 

```
tccli bmvpc ModifyVpcPeerConnection --cli-unfold-argument  \
    --Version 2018-06-25 \
    --VpcPeerConnectionId pcx-gapcv96p \
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

