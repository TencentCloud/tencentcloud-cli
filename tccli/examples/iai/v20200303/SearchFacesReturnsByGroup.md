**Example 1: 人脸搜索分库返回失败示例**



Input: 

```
tccli iai SearchFacesReturnsByGroup --cli-unfold-argument  \
    --Url http://test.image.myqcloud.com/testB.jpg \
    --MaxPersonNumPerGroup 5 \
    --GroupIds TencentShenZhenEmployee \
    --MaxFaceNum 1 \
    --MinFaceSize 40
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "FailedOperation.ImageDecodeFailed",
            "Message": "图片解码失败。"
        },
        "RequestId": "0e77ad29-ad65-4901-9efc-b49a6e0a357b"
    }
}
```

**Example 2: 人脸搜索分库返回成功示例**



Input: 

```
tccli iai SearchFacesReturnsByGroup --cli-unfold-argument  \
    --Url http://test.image.myqcloud.com/testA.jpg \
    --MaxPersonNumPerGroup 5 \
    --GroupIds TencentShenZhenEmployee \
    --MaxFaceNum 1 \
    --MinFaceSize 40
```

Output: 
```
{
    "Response": {
        "FaceNum": 1,
        "ResultsReturnsByGroup": [
            {
                "GroupCandidates": [
                    {
                        "Candidates": [
                            {
                                "PersonGroupInfos": [
                                    {
                                        "GroupId": "1002",
                                        "PersonExDescriptions": [
                                            "年龄",
                                            "性别"
                                        ]
                                    }
                                ],
                                "PersonId": "1002",
                                "Gender": 0,
                                "PersonName": "韦小宝",
                                "Score": 100,
                                "FaceId": "2875093635484912302"
                            }
                        ],
                        "GroupId": "Group1"
                    }
                ],
                "FaceRect": {
                    "Y": 46,
                    "X": 370,
                    "Height": 1,
                    "Width": 1
                },
                "RetCode": 0
            }
        ],
        "RequestId": "57b42b73-b978-45b9-8095-8f50e9642d35",
        "FaceModelVersion": "3.0"
    }
}
```

