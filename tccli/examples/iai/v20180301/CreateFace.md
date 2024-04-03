**Example 1: 错误示例**

已有人员最多再新增4张人脸图片

Input: 

```
tccli iai CreateFace --cli-unfold-argument  \
    --PersonId 1001 \
    --Urls http://test.image.myqcloud.com/testB.jpg http://test.image.myqcloud.com/testC.jpg http://test.image.myqcloud.com/testD.jpg http://test.image.myqcloud.com/testE.jpg http://test.image.myqcloud.com/testF.jpg
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "InvalidParameterValue.UploadFaceNumExceed",
            "Message": "一次最多上传四张人脸。"
        },
        "RequestId": "44506f79-2191-49bc-997b-748a566d781c"
    }
}
```

**Example 2: 增加人脸接口**

将一组人脸图片添加到一个人员中

Input: 

```
tccli iai CreateFace --cli-unfold-argument  \
    --PersonId 1001 \
    --Urls http://test.image.myqcloud.com/testA.jpg
```

Output: 
```
{
    "Response": {
        "SucFaceNum": 1,
        "SucFaceIds": [
            "2875186538564559728"
        ],
        "RetCode": [
            0
        ],
        "SucIndexes": [
            0
        ],
        "SucFaceRects": [
            {
                "X": 135,
                "Y": 42,
                "Width": 98,
                "Height": 136
            }
        ],
        "FaceModelVersion": "2.0",
        "RequestId": "07d63403-a199-4bbe-b9e0-692356ac738d"
    }
}
```

