**Example 1: 关闭自动签署**



Input: 

```
tccli ess ModifyExtendedService --cli-unfold-argument  \
    --Operator.ClientIp 8.8.8.8 \
    --Operator.UserId yDxjOUUgydjfxgnzUuO4zjEWA07rC2xl \
    --ServiceType OPEN_SERVER_SIGN \
    --Operate CLOSE \
    --Endpoint WEIXINAPP
```

Output: 
```
{
    "Response": {
        "OperateUrl": "",
        "RequestId": "s1703747615889528031"
    }
}
```

**Example 2: 开通自动签署**

1.开通企业自动签署（ServiceType 设置为WEIXINAPP）
2.设置Endpoint 为WEIXINAPP ，得到小程序链接，操作人可拿链接签署协议开通自动签署

Input: 

```
tccli ess ModifyExtendedService --cli-unfold-argument  \
    --Operator.ClientIp 8.8.8.8 \
    --Operator.UserId yDxjOUUgydjfxgnzUuO4zjEWA07rC2xl \
    --ServiceType OPEN_SERVER_SIGN \
    --Operate OPEN \
    --Endpoint WEIXINAPP
```

Output: 
```
{
    "Response": {
        "OperateUrl": "https://res.ess.tencent.cn/cdn/h5-activity/jump-mp.html?to=OPEN_SERVER_SIGN&request_token=yAABVUUckpt7e9gdUEcsWM19s3pglRL2&organizationId=yDxjOUUgydjf7zv3ACO4zjEC0AKihrfi&channelType=TENCENTCLOUD&expired_time=1703834015&login=1&verify=1",
        "RequestId": "s1703747615889528031"
    }
}
```

**Example 3: 管理不支持的扩展服务**



Input: 

```
tccli ess ModifyExtendedService --cli-unfold-argument  \
    --Operator.ClientIp 8.8.8.8 \
    --Operator.UserId yDxjOUUgydjfxgnzUuO4zjEWA07rC2xl \
    --ServiceType OPEN_SERVER \
    --Operate CLOSE \
    --Endpoint WEIXINAPP
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "InvalidParameter.ParamError",
            "Message": "非法的扩展服务类型OPEN_SERVER,请确认后重试"
        },
        "RequestId": "s1703747916297948958"
    }
}
```

