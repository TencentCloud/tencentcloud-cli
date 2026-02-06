**Example 1: 创建回源限速带宽限制**

创建 cn2.test-***a.online 的预热回源限制，配置预热的全球可用区（不含中国大陆）加速区域上回源带宽为100Mbps。

Input: 

```
tccli teo ModifyPrefetchOriginLimit --cli-unfold-argument  \
    --ZoneId zone-3***j8tqd \
    --DomainName cn2.test-***a.online \
    --Area Overseas \
    --Bandwidth 100 \
    --Enabled on
```

Output: 
```
{
    "Response": {
        "RequestId": "591c01a2-af21-4c09-af23-8f7d96832d01"
    }
}
```

**Example 2: 删除回源限速带宽限制**

删除 cn2.test-***a.online 的限制。

Input: 

```
tccli teo ModifyPrefetchOriginLimit --cli-unfold-argument  \
    --ZoneId zone-3***j8tqd \
    --DomainName cn2.test-***a.online \
    --Area Overseas \
    --Bandwidth 100 \
    --Enabled off
```

Output: 
```
{
    "Response": {
        "RequestId": "67a3d9f3-b852-4f6e-af7d-cc66ebc4fb08"
    }
}
```

