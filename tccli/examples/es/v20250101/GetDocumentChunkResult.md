**Example 1: 获取文档切片结果**



Input: 

```
tccli es GetDocumentChunkResult --cli-unfold-argument  \
    --TaskId 3041d1dc-1072-4025-a3c2-f8baea25801b
```

Output: 
```
{
    "Response": {
        "DocumentChunkResultUrl": "https://aisearch-xxx.cos.ap-xxx.myqcloud.com/%2F1257780094/2032/0eef71d5c6b94f4c9f77bf96a990dd93.zip?x-cos-security-token=xxx=sha1&q-ak=AKID_xxx&q-sign-time=1744101492%3B1744187892&q-key-time=1744101492%3B1744187892&q-header-list=host&q-url-param-list=x-cos-security-token&q-signature=xxx",
        "RequestId": "0b2bf3af-5671-45e8-a5db-xxx",
        "Status": 1,
        "Usage": {
            "PageNumber": 1,
            "TotalTokens": 118
        }
    }
}
```

