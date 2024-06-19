**Example 1: 接口调用成功示例**



Input: 

```
tccli lke GetReconstructDocumentResult --cli-unfold-argument  \
    --TaskId a9c6a9482c72412fa84445af84125531
```

Output: 
```
{
    "Response": {
        "DocumentRecognizeResultUrl": "https://document-restruction-1258344699.cos.ap-guangzhou.myqcloud.com/doc_parse/output_files/a9c6a9482c72412fa84445a44ss125531.zip?q-sign-algorithm=sha1&q-ak=AKIDlWFaadfHLNbidLwPqOrAKGzXrx40scL7l&q-sign-time=1715503711%3B1718804311&q-key-time=1718855711%3B1718804311&q-header-list=host&q-url-param-list=&q-signature=71b568b8632d7e45gertdc3d235ef68d41fdfe7f8",
        "FailedPages": [],
        "RequestId": "a37b0d0b-c3af-44bd-iuiu-632442644a80",
        "Status": "Success"
    }
}
```

