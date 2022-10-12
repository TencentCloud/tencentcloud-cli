**Example 1: 权属文件添加**



Input: 

```
tccli bma CreateCRRightFile --cli-unfold-argument  \
    --WorkId 1 \
    --FileList.0.FileUrl xxx \
    --FileList.0.FileType 1 \
    --FileList.0.ValidStartDate xxx \
    --FileList.0.ValidEndDate xxx
```

Output: 
```
{
    "Response": {
        "RequestId": "xxx",
        "FileIds": [
            1,
            2,
            3
        ]
    }
}
```

