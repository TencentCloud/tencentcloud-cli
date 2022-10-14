**Example 1: 创建文档**



Input: 

```
tccli lcic CreateDocument --cli-unfold-argument  \
    --SdkAppId 1 \
    --DocumentUrl xx \
    --DocumentName xx \
    --Owner xx \
    --TranscodeType 1 \
    --Permission 1 \
    --DocumentType xx \
    --DocumentSize 100
```

Output: 
```
{
    "Response": {
        "DocumentId": "xx",
        "RequestId": "213das"
    }
}
```

