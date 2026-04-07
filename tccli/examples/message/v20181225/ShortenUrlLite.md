**Example 1: 轻量长链换短链**

长链换短链-成功

Input: 

```
tccli message ShortenUrlLite --cli-unfold-argument  \
    --Url http://cloud.tencent.com/henry/testing/123 \
    --ValidPeriod 3600 \
    --Creator henryhzhao
```

Output: 
```
{
    "Response": {
        "ShortUrl": null,
        "RequestId": "8198f4a1-eadd-4c3e-80c8-ec933fee4b51"
    }
}
```

