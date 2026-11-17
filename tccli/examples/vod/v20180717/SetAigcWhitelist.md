**Example 1: 设置 AIGC 生视频任务的模型白名单和 IP 白名单**



Input: 

```
tccli vod SetAigcWhitelist --cli-unfold-argument  \
    --SubAppId 200000 \
    --AigcType Video \
    --ModelWhitelistSwitch ON \
    --IpWhitelistSwitch ON \
    --ModelWhitelist.0.ModelName Hunyuan \
    --ModelWhitelist.0.ModelVersion 1.5 \
    --IpWhitelist 1*.*.*.*/24
```

Output: 
```
{
    "Response": {
        "RequestId": "9ee3724d-6f5e-482a-9112-188e1c19d62a"
    }
}
```

