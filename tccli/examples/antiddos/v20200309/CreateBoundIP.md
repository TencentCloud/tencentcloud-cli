**Example 1: 绑定资产到高防包**

绑定资产到高防包

Input: 

```
tccli antiddos CreateBoundIP --cli-unfold-argument  \
    --BoundDevList.0.BizType cvm \
    --BoundDevList.0.Ip 1.1.1.1 \
    --BoundDevList.0.InstanceId id-xxx \
    --BoundDevList.0.DeviceType cvm \
    --BoundDevList.0.IspCode 1 \
    --BoundDevList.0.Domain www.abc.com \
    --Business bgp \
    --Id id-xxx \
    --UnBoundDevList.0.BizType cvm \
    --UnBoundDevList.0.Ip 1.1.1.1 \
    --UnBoundDevList.0.InstanceId id-xxx \
    --UnBoundDevList.0.DeviceType cvm \
    --UnBoundDevList.0.IspCode 1 \
    --UnBoundDevList.0.Domain www.abc.com \
    --CopyPolicy policy \
    --FilterRegion guangzhou
```

Output: 
```
{
    "Response": {
        "Success": {
            "Message": "msg",
            "Code": "200"
        },
        "RequestId": "reqid"
    }
}
```

