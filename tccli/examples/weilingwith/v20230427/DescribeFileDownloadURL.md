**Example 1: 获取文件下载地址**

获取文件下载地址返回结果

Input: 

```
tccli weilingwith DescribeFileDownloadURL --cli-unfold-argument  \
    --WorkspaceId 1016 \
    --FileId 3b81cb18-34ce-40f4-99e7-8fb0b9feeaeb \
    --ApplicationToken YzenL5LdGoxQM5gqJfCCoMDeGqUSsY78
```

Output: 
```
{
    "Response": {
        "RequestId": "d87de8da-6209-43df-8d87-7e6260850c5f",
        "Result": {
            "FileURL": "https://xxx.xxx"
        }
    }
}
```

