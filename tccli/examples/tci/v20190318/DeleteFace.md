**Example 1: 删除人脸**

删除人脸

Input: 

```
tccli tci DeleteFace --cli-unfold-argument  \
    --PersonId person_xxx \
    --FaceIdSet face_xxx \
    --LibraryId library_xxx
```

Output: 
```
{
    "Response": {
        "RequestId": "298fa9b6-38f3-48ce-b293-d447b6f7bedf",
        "FaceInfoSet": [
            {
                "PersonId": "person_xxx",
                "FaceUrl": "",
                "FaceId": "face_xxx",
                "ErrorMsg": ""
            }
        ]
    }
}
```

