**Example 1: 上传四层健康检查配置**



Input: 

```
tccli dayu CreateL4HealthConfig --cli-unfold-argument  \
    --Business bgpip \
    --Id bgpip-000000xe \
    --HealthConfig.0.Protocol TCP \
    --HealthConfig.0.VirtualPort 666 \
    --HealthConfig.0.Enable 1 \
    --HealthConfig.0.TimeOut 60 \
    --HealthConfig.0.Interval 300 \
    --HealthConfig.0.KickNum 3 \
    --HealthConfig.0.AliveNum 3 \
    --HealthConfig.0.KeepTime 60
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

