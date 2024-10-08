**Example 1: uploadFileResponse**

上传验签源文件响应

Input: 

```
tccli ca UploadFile --cli-unfold-argument  \
    --FileInfos.0.FileName rsa2.pdf \
    --FileInfos.0.FileBody data:application/pdf;base64,JVBERi0xLjcKJcKzx9gNCjEgMCBvYmoNPDwvTmFtZXMgPDwvRGVzd**********
```

Output: 
```
{
    "Response": {
        "FileIds": [
            "5419c4b9f60*****a4f77bb517b092f5"
        ],
        "RequestId": "805c9ab7-9372-4bea-b355-e89548552398",
        "TotalCount": 1
    }
}
```

**Example 2: uploadFile**

资源文件上传

Input: 

```
tccli ca UploadFile --cli-unfold-argument  \
    --FileInfos.0.FileName 1.pdf \
    --FileInfos.0.FileBody data:application/pdf;base64,JVBERi0xLjcKJcKzx9gNCjEgMCBvYmoNPDwvTmFtZXMgPDwvRGVzd***************
```

Output: 
```
{
    "Response": {
        "FileIds": [
            "b9e785d8d13349****9e460b04600e16"
        ],
        "RequestId": "25b59067-3b6b-4c5f-885d-9c12f4084f27",
        "TotalCount": 1
    }
}
```

