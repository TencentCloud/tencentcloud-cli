**Example 1: 查询模板文件下载地址**

查询模板文件下载地址

Input: 

```
tccli ioa DescribeTemplateFileDownloadUrl --cli-unfold-argument  \
    --TemplateFileName abc
```

Output: 
```
{
    "Response": {
        "Data": {
            "DownloadUrl": "abc"
        },
        "RequestId": "abc"
    }
}
```

