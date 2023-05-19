**Example 1: 绑定资产到高防包**

绑定资产到高防包

Input: 

```
tccli antiddos CreateBoundIP --cli-unfold-argument  \
    --BoundDevList.0.BizType abc \
    --BoundDevList.0.Ip abc \
    --BoundDevList.0.InstanceId abc \
    --BoundDevList.0.DeviceType abc \
    --BoundDevList.0.IspCode 1 \
    --BoundDevList.0.Domain abc \
    --Business abc \
    --Id abc \
    --UnBoundDevList.0.BizType abc \
    --UnBoundDevList.0.Ip abc \
    --UnBoundDevList.0.InstanceId abc \
    --UnBoundDevList.0.DeviceType abc \
    --UnBoundDevList.0.IspCode 1 \
    --UnBoundDevList.0.Domain abc \
    --CopyPolicy abc \
    --FilterRegion abc
```

Output: 
```
{
    "Response": {
        "Success": {
            "Message": "abc",
            "Code": "abc"
        },
        "RequestId": "abc"
    }
}
```

