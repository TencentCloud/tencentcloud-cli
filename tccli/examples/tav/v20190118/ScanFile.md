**Example 1: tav文件上传扫描**



Input: 

```
tccli tav ScanFile --cli-unfold-argument  \
    --Key d12790cf44382a3c15e4e8c63e41e74d \
    --Sample http://10.195.2.97/download?md5 \
    --Md5 0f600011f6abb02f6a117e1efb952a3c
```

Output: 
```
{
    "Response": {
        "Status": 200,
        "Info": "scan success",
        "Data": "",
        "RequestId": "00f29851-2408-4818-b66c-3b2d2ba4196f"
    }
}
```

