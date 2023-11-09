**Example 1: 获取上传文件返回地址**

正常返回结果

Input: 

```
tccli weilingwith DescribeFileUploadURL --cli-unfold-argument  \
    --WorkspaceId 1016 \
    --FileName a \
    --FileSize 10 \
    --FileExpireTime 1693411200 \
    --ApplicationToken YzenL5LdGoxQM5gqJfCCoMDeGqUSsY78
```

Output: 
```
{
    "Response": {
        "RequestId": "6d75ec52-741b-4579-bb7e-1c554e3a153c",
        "Result": {
            "DownloadURL": "https://wetwin-managr-xxx",
            "FileId": "dcdc04b4-8417-4b4c-8658-38ea09a67dde",
            "UploadURL": "https://wetwin-manager-xxx"
        }
    }
}
```

