**Example 1: 上传文件。**

上传文件。

Input: 

```
tccli hunyuan FilesUploads --cli-unfold-argument  \
    --Name 云API产品简介.pdf \
    --URL https://main.qcloudimg.com/raw/document/product/pdf/1278_46794_cn.pdf
```

Output: 
```
{
    "Response": {
        "RequestId": "a5f3568b-45dc-4cc9-9fef-268768b0dbca",
        "ID": "file-YbhlphnNEsjRoKTEXukAqNZZ",
        "Object": "file",
        "Bytes": 422915,
        "CreatedAt": 1722513746,
        "Filename": "云API产品简介.pdf",
        "Purpose": "file-extract"
    }
}
```

