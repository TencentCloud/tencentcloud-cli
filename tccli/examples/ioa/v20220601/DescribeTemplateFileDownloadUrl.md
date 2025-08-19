**Example 1: 查询模板文件下载地址**

查询模板文件下载地址

Input: 

```
tccli ioa DescribeTemplateFileDownloadUrl --cli-unfold-argument  \
    --TemplateFileName tsta.csv
```

Output: 
```
{
    "Response": {
        "Data": {
            "DownloadUrl": "htt://cos.1x.com/daca/sav11v"
        },
        "RequestId": "fgsdfgsdfg23422"
    }
}
```

