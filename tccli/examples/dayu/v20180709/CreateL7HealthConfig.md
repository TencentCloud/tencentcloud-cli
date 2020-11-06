**Example 1: 上传七层健康检查配置**



Input: 

```
tccli dayu CreateL7HealthConfig --cli-unfold-argument  \
    --Business bgpip \
    --Id bgpip-000000xe \
    --HealthConfig.0.Protocol https \
    --HealthConfig.0.Domain 443 \
    --HealthConfig.0.Enable 1 \
    --HealthConfig.0.Interval 300 \
    --HealthConfig.0.KickNum 3 \
    --HealthConfig.0.AliveNum 3 \
    --HealthConfig.0.Method HEAD \
    --HealthConfig.0.StatusCode 15 \
    --HealthConfig.0.Url /
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

