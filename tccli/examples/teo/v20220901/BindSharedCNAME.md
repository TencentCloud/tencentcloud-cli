**Example 1: 绑定共享 CNAME**

将 ZoneId 为 zone-225qgrnvbi9w 的站点下的域名 a.qq.com 和 b.qq.com 绑定至共享 CNAME qq.com.sai2ig51kaa5.share.dnse5.com，域名 api.qq.com 和 img.qq.com 绑定至共享 CNAME config.qq.com.sai2ig51kaa5.share.dnse5.com。

Input: 

```
tccli teo BindSharedCNAME --cli-unfold-argument  \
    --ZoneId zone-225qgrnvbi9w \
    --BindType bind \
    --BindSharedCNAMEMaps.0.SharedCNAME qq.com.sai2ig51kaa5.share.dnse5.com \
    --BindSharedCNAMEMaps.0.DomainNames a.qq.com b.qq.com \
    --BindSharedCNAMEMaps.1.SharedCNAME config.qq.com.sai2ig51kaa5.share.dnse5.com \
    --BindSharedCNAMEMaps.1.DomainNames api.qq.com img.qq.com
```

Output: 
```
{
    "Response": {
        "RequestId": "5e0a2b4e-df6d-4d2a-ac39-1706cbf8a707"
    }
}
```

**Example 2: 解绑共享 CNAME**

将 ZoneId 为 zone-225qgrnvbi9w 的站点下的域名 a.qq.com 和共享 CNAME qq.com.sai2ig51kaa5.share.dnse5.com 解绑。

Input: 

```
tccli teo BindSharedCNAME --cli-unfold-argument  \
    --ZoneId zone-225qgrnvbi9w \
    --BindType unbind \
    --BindSharedCNAMEMaps.0.SharedCNAME qq.com.sai2ig51kaa5.share.dnse5.com \
    --BindSharedCNAMEMaps.0.DomainNames a.qq.com
```

Output: 
```
{
    "Response": {
        "RequestId": "5e0a2b4e-df6d-5d3a-ac39-1706cbf8a708"
    }
}
```

