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
        "DocumentParseResultUrl": "https://aisearch-xxxx.cos.ap-guangzhou.myqcloud.com/%2F1257780094/2025/87a8419e7e7d4bd9ad17267c47d12168.zip?x-cos-security-token=6VP365zlkuYclNSS8Uo2nO0HnR8EnMpa3af95a3e21d25bc893099fa2755135125OWpJjDZaOCMgmOglpve2Riw_eQhuqLM0X-s-TelbIipYTGRWgodzr4MspocQuTqi-qxIWjgLlCyv52JP2uA-ebvnGjaqsfxDZiaQf8SLEvv_OpdZ_DWdf2GVFJlxcMkyRb3swd900raxsnGuq1HOq2apiWxIqdyKD2XNeicqJiKvXBIwNozOhUt9bj9BBYLOiQOjHw5dLFDJM6xa53b9X2Z1LJKK53FlNJ5buCZ9Up18vKJn1YtFMAxvMYY-N1peQpzBo6OC-nj5ObvGYYSz-OOy3edOkaHzHksKuxBz181sk2EXrWf4NyF4pbuKM0YkFYek_d06s9n3MBsqXBIv79U3vmSfpjsTM7I26idRZg&q-sign-algorithm=sha1&q-ak=AKIDlCtP1SmwsERqUnRAwLlOZ21NbUGlevaln-DCwJZcft9vsiPNHgEMiwusHrhFpCa0&q-sign-time=1744014678%3B1744101078&q-key-time=1744014678%3B1744101078&q-header-list=host&q-url-param-list=x-cos-security-token&q-signature=ef15228dff60abfe0f7a4e51df7d81cf1fcff767",
        "FailedPages": null,
        "RequestId": "7da936b2-8d10-42bd-b65f-8d10ae99927a",
        "Status": 1
    }
}
```

