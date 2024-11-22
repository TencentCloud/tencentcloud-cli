**Example 1: 获取人员列表成功示例**



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
                ],
                "CreationTimestamp": 1594642823572
            }
        ],
        "PersonNum": 1,
        "FaceNum": 1,
        "FaceModelVersion": "3.0",
        "RequestId": "337d1bb5-3f88-4681-9291-5194f478f0d1"
    }
}
```

**Example 2: 获取人员列表失败示例**



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

