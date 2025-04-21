**Example 1: 上传logo图标**

上传logo图标，将logo内容base64编码传输，上传成功返回名称。

Input: 

```
tccli ioa UploadLogo --cli-unfold-argument  \
    --LogoName logoFileName \
    --LogoContent logoFileContent base64
```

Output: 
```
{
    "Response": {
        "Data": {
            "FileKey": "logoFileName"
        },
        "RequestId": "abc"
    }
}
```

