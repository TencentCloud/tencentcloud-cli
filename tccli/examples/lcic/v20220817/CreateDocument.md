**Example 1: 创建文档**



Input: 

```
tccli lcic CreateDocument --cli-unfold-argument  \
    --SdkAppId 1 \
    --DocumentUrl abc \
    --DocumentName abc \
    --Owner abc \
    --TranscodeType 1 \
    --Permission 1 \
    --DocumentType abc \
    --DocumentSize 1 \
    --AutoHandleUnsupportedElement True
```

Output: 
```
{
    "Response": {
        "DocumentId": "abc",
        "RequestId": "abc"
    }
}
```

