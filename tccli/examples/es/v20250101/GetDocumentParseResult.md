**Example 1: 获取文档解析任务结果**



Input: 

```
tccli es GetDocumentParseResult --cli-unfold-argument  \
    --TaskId 3cce395a-fe9e-460f-9b19-8920d15867e3
```

Output: 
```
{
    "Response": {
        "DocumentParseResultUrl": "https://aisearch-xxxx.cos.ap-xxx.myqcloud.com/%2F1257780094/2025/87a8419e7e7d4bd9ad17267c47d12168.zip?x-cos-security-token=xxx&q-sign-algorithm=sha1&q-ak=xxx&q-sign-time=1744014678%3B1744101078&q-key-time=1744014678%3B1744101078&q-header-list=host&q-url-param-list=x-cos-security-token&q-signature=xxx",
        "FailedPages": null,
        "RequestId": "7da936b2-8d10-42bd-b65f-8d10ae99927a",
        "Status": 1
    }
}
```

