**Example 1: 获取结果成功**

获取核身结果

Input: 

```
tccli faceid GetFaceIdResultIntl --cli-unfold-argument  \
    --SdkToken aeee6d62-b2b2-4634-9662-919a5ac729ab
```

Output: 
```
{
    "Response": {
        "Result": "0",
        "Description": "Success",
        "BestFrame": "AAAAHGZ0eXBtcDQyAAAAAWlzb2...",
        "Video": "/9j/4AAQSkZJRgABAQAASABIAAD/4QBMR...",
        "ActionVideo": "AAAAHGZ0eXBtcDQyAAAAAWlzb21tcD...",
        "Similarity": 98.8,
        "Extra": "",
        "RequestId": "aea12d62-b2b2-4634-9662-919a5ac729ab"
    }
}
```

