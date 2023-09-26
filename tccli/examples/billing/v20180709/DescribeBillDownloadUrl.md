**Example 1: 获取账单下载链接**

获取账单下载链接

Input: 

```
tccli billing DescribeBillDownloadUrl --cli-unfold-argument  \
    --FileType billPack \
    --Month 2023-08
```

Output: 
```
{
    "Response": {
        "DownloadUrl": "http://xxxxxxxxxxxxxxxxx",
        "Ready": 1,
        "RequestId": "3efd37d8-68aa-4bfc-8f8c-f8a0197f9931"
    }
}
```

