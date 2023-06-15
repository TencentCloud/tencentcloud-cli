**Example 1: 添加CDN加速域名**

添加CDN加速域名

Input: 

```
tccli vod CreateCDNDomain --cli-unfold-argument  \
    --Domain myexample.com \
    --Config.Area mainland \
    --Config.Origin.Origins src.myexample.com \
    --Config.Origin.OriginType domain
```

Output: 
```
{
    "Response": {
        "RequestId": "12ae8d8e-dce3-4551-9d4b-5594145287e1"
    }
}
```

