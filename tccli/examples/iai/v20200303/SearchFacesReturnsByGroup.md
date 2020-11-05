**Example 1: Searching for face with results returned by group**



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
                "RetCode": 0,
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
                            "PersonName": "John Smith",
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
        "FaceModelVersion": "3.0",
        "RequestId": "57b42b73-b978-45b9-8095-8f50e9642d35"
    }
}
```

