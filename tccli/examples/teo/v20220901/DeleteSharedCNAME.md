**Example 1: 删除共享 CNAME**

删除 ZoneId 为 zone-225qgrnvbi9w 的站点下的共享 CNAME qq.com.225qgrnvbi9w.share.dnse5.com。

Input: 

```
tccli teo DeleteSharedCNAME --cli-unfold-argument  \
    --SharedCNAME qq.com.225qgrnvbi9w.share.dnse5.com \
    --ZoneId zone-225qgrnvbi9w
```

Output: 
```
{
    "Response": {
        "RequestId": "5e0a2b4e-df6d-4d2a-ac39-1706cbf8a707"
    }
}
```

