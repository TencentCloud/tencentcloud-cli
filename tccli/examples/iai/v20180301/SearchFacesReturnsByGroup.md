**Example 1: 人脸搜索分库返回接口**



Input: 

```
tccli iai SearchFacesReturnsByGroup --cli-unfold-argument  \
    --Url http://test.image.myqcloud.com/testA.jpg\
    --MaxFaceNum 1\
    --MinFaceSize 40\
    --MaxPersonNumPerGroup 5\
    --GroupIds TencentShenZhenEmployee
```

Output: 
```
{
    "Response": {
        "ResultsReturnsByGroup": [
            {
                "FaceRect": {
                    "X": 370,
                    "Y": 46,
                    "Width": 75,
                    "Height": 80
                },
                "GroupCandidates": [
                    {
                        "GroupId": "Group1",
                        "Candidates": {
                            "PersonId": "1001",
                            "FaceId": "2875093635484912302",
                            "Score": 100,
                            "PersonName": "张三",
                            "Gender": 0,
                            "PersonGroupInfos": [
                                {
                                    "GroupId": "abc",
                                    "PersonExDescriptions": [
                                        "description1",
                                        "description2"
                                    ]
                                }
                            ]
                        }
                    }
                ]
            }
        ],
        "FaceNum": 1,
        "RequestId": "57b42b73-b978-45b9-8095-8f50e9642d35"
    }
}
```

