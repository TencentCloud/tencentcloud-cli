**Example 1: Searching for face**



Input: 

```
tccli iai SearchFaces --cli-unfold-argument  \
    --Url http://test.image.myqcloud.com/testA.jpg \
    --MaxFaceNum 1 \
    --MinFaceSize 40 \
    --MaxPersonNum 5 \
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
                        "PersonId": "1001",
                        "FaceId": "2875093635484912302",
                        "PersonName": "Jerry",
                        "Gender": 0,
                        "Score": 100,
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
                ],
                "FaceRect": {
                    "X": 370,
                    "Y": 46,
                    "Width": 75,
                    "Height": 75
                }
            }
        ],
        "FaceNum": 1,
        "FaceModelVersion": "3.0",
        "RequestId": "57b42b73-b978-45b9-8095-8f50e9642d35"
    }
}
```

**Example 2: Sample error**

`MaxFaceNum` cannot be above 10.

Input: 

```
tccli iai SearchFaces --cli-unfold-argument  \
    --Url http://test.image.myqcloud.com/testA.jpg \
    --MaxFaceNum 11 \
    --GroupIds TencentShenZhenEmployee
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "FailedOperation.SearchFacesExceed",
            "Message": "The number of faces searched for exceeds the limit."
        },
        "RequestId": "f04ba2f3-532c-4207-9caa-6e818ded7fb9"
    }
}
```

**Example 3: Sample error - 2**

Incorrect image URL.

Input: 

```
tccli iai SearchFaces --cli-unfold-argument  \
    --Url http://test.image.myqcloud.com/testA \
    --GroupIds TencentShenZhenEmployee
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "FailedOperation.ImageDownloadError",
            "Message": "An error occurred while downloading the image."
        },
        "RequestId": "527ecffe-4c6a-47c9-8217-4dd2e3f018da"
    }
}
```

