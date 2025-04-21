**Example 1: 获取下载文件cos地址**

获取下载文件cos地址

Input: 

```
tccli ioa DescribeTemplateFileUploadUrl --cli-unfold-argument  \
    --FileName abc
```

Output: 
```
{
    "Response": {
        "Data": {
            "UploadURL": "abc",
            "UploadToken": "abc",
            "ExpireAt": "abc"
        },
        "RequestId": "abc"
    }
}
```

