**Example 1: 创建一个海外普通的四层实例**

在 ZoneId 为 zone-3kq782jghthh 的站点下创建一个名称为 proxy-name，加速区域为全球加速（不含中国大陆）的四层实例。

Input: 

```
tccli teo CreateL4Proxy --cli-unfold-argument  \
    --ZoneId zone-3kq782jghthh \
    --ProxyName proxy-name \
    --Area overseas
```

Output: 
```
{
    "Response": {
        "ProxyId": "sid-3kq7it9slfmc",
        "RequestId": "37752cc1-7d73-47b4-801a-31a6a38c4dea"
    }
}
```

