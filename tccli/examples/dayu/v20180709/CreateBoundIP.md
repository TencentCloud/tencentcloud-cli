**Example 1: 绑定IP到高防包实例**



Input: 

```
tccli dayu CreateBoundIP --cli-unfold-argument  \
    --Business bgp \
    --Id bgp-000000xe \
    --BoundDevList.0.Ip 1.1.1.1 \
    --BoundDevList.0.BizType public \
    --BoundDevList.0.DeviceType cvm \
    --BoundDevList.0.InstanceId ins-f2f9ssbo \
    --CopyPolicy yes
```

Output: 
```
{
    "Response": {
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397",
        "Success": {
            "Code": "Success",
            "Message": "Success"
        }
    }
}
```

