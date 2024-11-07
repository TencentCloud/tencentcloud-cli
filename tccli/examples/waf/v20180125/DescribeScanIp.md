**Example 1: 查询扫描ip**



Input: 

```
tccli waf DescribeScanIp --cli-unfold-argument  \
    --Ip 1.1.1.1
```

Output: 
```
{
    "Response": {
        "Bussiness": "微信支付",
        "Characteristic": "腾讯业务回调",
        "Descibe": "微信支付通过回调出口 IP 持续对网络环境进行监测，以达到优化回调效率、提升用户体验的目的。",
        "Referer": "https://developers.weixin.qq.com/community/develop/doc/000a2e2dcd48c0f126f08ef4562000",
        "Demo": "业务回调",
        "Target": "数据传输",
        "Purpose": "保障回调顺畅、服务稳定",
        "Announcement": "此 IP为 微信支付 的扫描 IP，将定期对您的 数据传输 进行检测，以 保障回调顺畅、服务稳定，若您发现来自此 IP 的扫描行为，请进行放行或加白...",
        "RequestId": "aqdraqerqw12313sdff"
    }
}
```

