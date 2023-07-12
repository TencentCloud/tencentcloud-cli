**Example 1: 批量删除加速域名**

删除指定ID加速域名。

Input: 

```
tccli teo DeleteAccelerationDomains --cli-unfold-argument  \
    --DomainNames qq.com \
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

