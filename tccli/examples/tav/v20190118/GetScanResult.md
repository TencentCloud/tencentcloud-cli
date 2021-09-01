**Example 1: tav文件上传扫描结果查询**



Input: 

```
tccli tav GetScanResult --cli-unfold-argument  \
    --Key d12790cf44382a3c15e4e8c63e41e74d \
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

