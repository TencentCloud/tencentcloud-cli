**Example 1: 预热资源**



Input: 

```
tccli hcdn PreloadCache --cli-unfold-argument  \
    --FileItemSet.0.FileUrl https://www.qq.com/xx1.flv \
    --FileItemSet.0.FileSize 1024000 \
    --FileItemSet.0.FileShaSum 8f10270495ce790a2f9140600d57fc1251976244 \
    --FileItemSet.1.FileUrl https://www.qq.com/xx2.flv \
    --FileItemSet.1.FileSize 1024000 \
    --FileItemSet.1.FileShaSum 8f10270495ce790a2f9140600d57fc1251976245
```

Output: 
```
{
    "Response": {
        "RequestId": "4db38754-c2f4-4190-862f-557ff1654317",
        "TaskId": "20830af4-3d4d-46f3-b06b-88f15028aaec"
    }
}
```

