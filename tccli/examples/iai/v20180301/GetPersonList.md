**Example 1: 错误示例**

人员库ID不存在

Input: 

```
tccli iai GetPersonList --cli-unfold-argument  \
    --GroupId ZhuYuanDormitory \
    --Offset 0 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "InvalidParameterValue.GroupIdNotExist",
            "Message": "人员库ID不存在。"
        },
        "RequestId": "b7c0cd81-d621-465f-8fd6-86a6b49e67be"
    }
}
```

**Example 2: 获取人员列表接口**



Input: 

```
tccli iai GetPersonList --cli-unfold-argument  \
    --GroupId ZhuYuanDormitoryNo1 \
    --Offset 0 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "PersonInfos": [
            {
                "PersonName": "Junly",
                "PersonId": "2001",
                "Gender": 1,
                "PersonExDescriptions": [
                    "计算机学院",
                    "软件工程",
                    "15级",
                    "3150108080"
                ],
                "FaceIds": [
                    "2877244861637985315"
                ]
            }
        ],
        "PersonNum": 1,
        "FaceNum": 1,
        "FaceModelVersion": "3.0",
        "RequestId": "337d1bb5-3f88-4681-9291-5194f478f0d1"
    }
}
```

**Example 3: 获取人员列表接口-2**

获取指定人员库中的人员列表

Input: 

```
tccli iai GetPersonList --cli-unfold-argument  \
    --GroupId TencentShenZhenEmployee \
    --Offset 0 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "PersonInfos": [
            {
                "PersonName": "evanliao",
                "PersonId": "1001",
                "Gender": 1,
                "PersonExDescriptions": [
                    "云与智慧产业事业群",
                    "大数据及人工智能产品中心",
                    "人脸识别产品组"
                ],
                "FaceIds": [
                    "2877242150180891493"
                ]
            }
        ],
        "PersonNum": 1,
        "FaceNum": 1,
        "FaceModelVersion": "3.0",
        "RequestId": "aa292f16-27d9-423b-9048-cdd43f6e4156"
    }
}
```

