**Example 1: 创建人员接口**



Input: 

```
tccli iai CreatePerson --cli-unfold-argument  \
    --GroupId ZhuYuanDormitoryNo1 \
    --PersonName Junly \
    --PersonId 2001 \
    --Gender 1 \
    --Url http://test.image.myqcloud.com/testB.jpg \
    --PersonExDescriptionInfos.0.PersonExDescriptionIndex 0 \
    --PersonExDescriptionInfos.0.PersonExDescription 计算机学院 \
    --PersonExDescriptionInfos.1.PersonExDescriptionIndex 1 \
    --PersonExDescriptionInfos.1.PersonExDescription 软件工程 \
    --PersonExDescriptionInfos.2.PersonExDescriptionIndex 2 \
    --PersonExDescriptionInfos.2.PersonExDescription 15级 \
    --PersonExDescriptionInfos.3.PersonExDescriptionIndex 3 \
    --PersonExDescriptionInfos.3.PersonExDescription 3150808
```

Output: 
```
{
    "Response": {
        "FaceId": "3454816969590585885",
        "SimilarPersonId": "",
        "FaceRect": {
            "X": 172,
            "Y": 122,
            "Width": 178,
            "Height": 228
        },
        "FaceModelVersion": "3.0",
        "RequestId": "738a2fb0-bd4b-4cf6-9c91-18d50978d76b"
    }
}
```

**Example 2: 创建人员接口-2**

创建人员

Input: 

```
tccli iai CreatePerson --cli-unfold-argument  \
    --GroupId TencentShenZhenEmployee \
    --PersonName evanliao \
    --PersonId 1001 \
    --Gender 1 \
    --Url http://test.image.myqcloud.com/testA.jpg \
    --PersonExDescriptionInfos.0.PersonExDescriptionIndex 0 \
    --PersonExDescriptionInfos.0.PersonExDescription 云与智慧产业事业群 \
    --PersonExDescriptionInfos.1.PersonExDescriptionIndex 1 \
    --PersonExDescriptionInfos.1.PersonExDescription 人工智能产品中心 \
    --PersonExDescriptionInfos.2.PersonExDescriptionIndex 2 \
    --PersonExDescriptionInfos.2.PersonExDescription 人脸识别产品组
```

Output: 
```
{
    "Response": {
        "FaceId": "3454816969590585881",
        "SimilarPersonId": "",
        "FaceRect": {
            "X": 172,
            "Y": 122,
            "Width": 178,
            "Height": 228
        },
        "FaceModelVersion": "3.0",
        "RequestId": "269a6bc0-0016-47e8-a63d-517ce4052b0e"
    }
}
```

**Example 3: 错误示例**

人员ID不可重复

Input: 

```
tccli iai CreatePerson --cli-unfold-argument  \
    --GroupId ZhuYuanDormitoryNo1 \
    --PersonName Cheng \
    --PersonId 1001 \
    --Gender 2 \
    --Url http://test.image.myqcloud.com/testD.jpg
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "InvalidParameterValue.PersonIdAlreadyExist",
            "Message": "人员ID已经存在。人员ID不可重复。"
        },
        "RequestId": "76dedef7-af27-4a20-9064-c5ef3133926d"
    }
}
```

**Example 4: 错误示例-2**

人员库ID不存在

Input: 

```
tccli iai CreatePerson --cli-unfold-argument  \
    --GroupId ShenZhenCitizen \
    --PersonName Siccy \
    --PersonId 3001 \
    --Gender 2 \
    --Url http://test.image.myqcloud.com/testC.jpg
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "InvalidParameterValue.GroupIdNotExist",
            "Message": "人员库ID不存在。"
        },
        "RequestId": "dfa512fc-fd07-4bf1-a292-cb497b620857"
    }
}
```

