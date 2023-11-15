**Example 1: 删除公网IP/域名**

删除公网IP/域名

Input: 

```
tccli csip DeleteDomainAndIp --cli-unfold-argument  \
    --Content.0.Asset abc \
    --RetainPath 0 \
    --IgnoreAsset 0 \
    --Tags.0.TagKey abc \
    --Tags.0.TagValue abc \
    --Type abc
```

Output: 
```
{
    "Response": {
        "Data": 0,
        "RequestId": "abc"
    }
}
```

