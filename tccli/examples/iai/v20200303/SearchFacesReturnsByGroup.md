**Example 1: 人脸搜索分库返回接口**



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
                                        "GroupId": "abc",
                                        "PersonExDescriptions": [
                                            "description1",
                                            "description2"
                                        ]
                                    }
                                ],
                                "PersonId": "1001",
                                "Gender": 0,
                                "PersonName": "张三",
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

