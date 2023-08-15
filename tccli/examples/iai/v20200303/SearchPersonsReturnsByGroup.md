**Example 1: 人员搜索分库返回接口**



Input: 

```
tccli iai SearchPersonsReturnsByGroup --cli-unfold-argument  \
    --Url http://test.image.myqcloud.com/testA.jpg \
    --MaxFaceNum 1 \
    --MinFaceSize 40 \
    --MaxPersonNumPerGroup 5 \
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
                    "X": 375,
                    "Y": 37,
                    "Width": 63,
                    "Height": 82
                },
                "GroupCandidates": [
                    {
                        "GroupId": "TencentShenZhenEmployee",
                        "Candidates": [
                            {
                                "PersonId": "testtest3",
                                "FaceId": "",
                                "Score": 100,
                                "PersonName": null,
                                "Gender": null,
                                "PersonGroupInfos": null
                            }
                        ]
                    }
                ]
            }
        ],
        "PersonNum": 1,
        "FaceModelVersion": "3.0",
        "RequestId": "c8a06ec5-ecb4-4dd7-a8c8-ce5e675495c2"
    }
}
```

**Example 2: 错误示例**



Input: 

```
tccli iai SearchPersonsReturnsByGroup --cli-unfold-argument  \
    --Url http://test.image.myqcloud.com/testB.jpg \
    --MaxFaceNum 1 \
    --MinFaceSize 40 \
    --MaxPersonNumPerGroup 5 \
    --GroupIds TencentShenZhenEmployee
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "FailedOperation.ImageDownloadError",
            "Message": "图片下载错误。"
        },
        "RequestId": "527ecffe-4c6a-47c9-8217-4dd2e3f018da"
    }
}
```

