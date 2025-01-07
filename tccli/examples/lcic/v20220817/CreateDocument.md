**Example 1: 创建文档**



Input: 

```
tccli lcic CreateDocument --cli-unfold-argument  \
    --SdkAppId 329013 \
    --DocumentUrl http://4323ba94-27a5bca82d6b.doc \
    --DocumentName 课堂文档 \
    --Owner Tom \
    --TranscodeType 1 \
    --Permission 1 \
    --DocumentType doc \
    --DocumentSize 1 \
    --AutoHandleUnsupportedElement True
```

Output: 
```
{
    "Response": {
        "DocumentId": "wuplop",
        "RequestId": "bb9c8d-4236-419b-8c39-572234jifsns7"
    }
}
```

