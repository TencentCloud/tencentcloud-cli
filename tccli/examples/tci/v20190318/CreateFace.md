**Example 1: 添加人脸**

添加人脸

Input: 

```
tccli tci CreateFace --cli-unfold-argument  \
    --PersonId person_xxx \
    --LibraryId library_xxx \
    --Urls http://xxx.jpg
```

Output: 
```
{
    "Response": {
        "RequestId": "9e5e3ab1-5bd6-404e-9593-74ab9e6aaf79",
        "FaceInfoSet": [
            {
                "PersonId": "person_xxx",
                "FaceUrl": "https://soe-1255701415.cos.ap-beijing.myqcloud.com/251006279/library_1552907886376820469/person_1553000279384479226589/59d46161b44bb83ce496573b6c20cd54.png",
                "FaceId": "xxx",
                "ErrorMsg": ""
            }
        ]
    }
}
```

