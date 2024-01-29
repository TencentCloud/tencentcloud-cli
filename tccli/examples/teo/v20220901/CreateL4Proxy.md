**Example 1: 新建加速区域为中国大陆可用区的四层代理实例**

在 ZoneId 为 zone-2jc2xy3hr7f7 的站点下创建一个名称为 test，加速区域为中国大陆可用区的四层实例。

Input: 

```
tccli teo CreateL4Proxy --cli-unfold-argument  \
    --ProxyName test \
    --ZoneId zone-2jc2xy3hr7f7 \
    --Area mainland
```

Output: 
```
{
    "Response": {
        "ProxyId": "sid-2jc2hl2hr8f7",
        "RequestId": "0se57a54-cc42-11ed-8efb-525401a961b1"
    }
}
```

**Example 2: 新建加速区域为全球可用区（不含中国大陆），开启独立 DDoS 防护的四层代理实例**

在 ZoneId 为 zone-2jc2xy3hr7f7 的站点下创建一个名称为 test，加速区域为全球可用区（不含中国大陆）的四层实例，且开启独立 DDoS 防护，提供加速区域范围的全力防护。

Input: 

```
tccli teo CreateL4Proxy --cli-unfold-argument  \
    --ZoneId zone-2jc2xy3hr7f7 \
    --ProxyName test \
    --Area overseas \
    --DDosProtectionConfig.LevelOverseas ANYCAST_ALLIN
```

Output: 
```
{
    "Response": {
        "ProxyId": "sid-2jc2hl2hr8f7",
        "RequestId": "0se57a54-cc42-11ed-8efb-525401a961b1"
    }
}
```

