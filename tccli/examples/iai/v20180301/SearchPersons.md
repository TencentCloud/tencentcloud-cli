**Example 1: 人员搜索接口**



Input: 

```
tccli iai SearchPersons --cli-unfold-argument  \
    --Url http://test.image.myqcloud.com/testA.jpg \
    --MaxFaceNum 2 \
    --MinFaceSize 40 \
    --MaxPersonNum 3 \
    --GroupIds TencentShenZhenEmployee
```

Output: 
```
{
    "Response": {
        "Results": [
            {
                "RetCode": 0,
                "Candidates": [
                    {
                        "PersonId": "person1",
                        "FaceId": "",
                        "Score": 100,
                        "PersonName": null,
                        "Gender": null,
                        "PersonGroupInfos": null
                    },
                    {
                        "PersonId": "person2",
                        "FaceId": "",
                        "Score": 60,
                        "PersonName": null,
                        "Gender": null,
                        "PersonGroupInfos": null
                    },
                    {
                        "PersonId": "person3",
                        "FaceId": "",
                        "Score": 50,
                        "PersonName": null,
                        "Gender": null,
                        "PersonGroupInfos": null
                    }
                ],
                "FaceRect": {
                    "X": 139,
                    "Y": 59,
                    "Width": 124,
                    "Height": 162
                }
            },
            {
                "RetCode": 0,
                "Candidates": [
                    {
                        "PersonId": "person2",
                        "FaceId": "",
                        "Score": 100,
                        "PersonName": null,
                        "Gender": null,
                        "PersonGroupInfos": null
                    },
                    {
                        "PersonId": "person1",
                        "FaceId": "",
                        "Score": 60,
                        "PersonName": null,
                        "Gender": null,
                        "PersonGroupInfos": null
                    },
                    {
                        "PersonId": "person3",
                        "FaceId": "",
                        "Score": 20,
                        "PersonName": null,
                        "Gender": null,
                        "PersonGroupInfos": null
                    }
                ],
                "FaceRect": {
                    "X": 328,
                    "Y": 70,
                    "Width": 119,
                    "Height": 162
                }
            }
        ],
        "PersonNum": 5,
        "FaceModelVersion": "3.0",
        "RequestId": "c4608852-ff60-4a01-8dc3-367f6046baaf"
    }
}
```

**Example 2: 错误示例**

图片URL错误

Input: 

```
tccli iai SearchPersons --cli-unfold-argument  \
    --Url http://test.image.myqcloud.com/testA \
    --GroupIds TencentShenZhenEmployee
```

Output: 
```
{
    "Response": {
        "RequestId": "527ecffe-4c6a-47c9-8217-4dd2e3f018da"
    }
}
```

