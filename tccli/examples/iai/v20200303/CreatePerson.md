**Example 1: Creating person**



Input: 

```
tccli iai CreatePerson --cli-unfold-argument  \
    --GroupId ZhuYuanDormitoryNo1 \
    --PersonName Junly \
    --PersonId 2001 \
    --Gender 1 \
    --Url http://test.image.myqcloud.com/testB.jpg \
    --PersonExDescriptionInfos.0.PersonExDescriptionIndex 0 \
    --PersonExDescriptionInfos.0.PersonExDescription 'School of Computing' \
    --PersonExDescriptionInfos.1.PersonExDescriptionIndex 1 \
    --PersonExDescriptionInfos.1.PersonExDescription 'Software Engineering' \
    --PersonExDescriptionInfos.2.PersonExDescriptionIndex 2 \
    --PersonExDescriptionInfos.2.PersonExDescription '15 \
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

**Example 2: Creating person - 2**

This example shows you how to create a person.

Input: 

```
tccli iai CreatePerson --cli-unfold-argument  \
    --GroupId TencentShenZhenEmployee \
    --PersonName evanliao \
    --PersonId 1001 \
    --Gender 1 \
    --Url http://test.image.myqcloud.com/testA.jpg \
    --PersonExDescriptionInfos.0.PersonExDescriptionIndex 0 \
    --PersonExDescriptionInfos.0.PersonExDescription 'Cloud and Smart Industries Group' \
    --PersonExDescriptionInfos.1.PersonExDescriptionIndex 1 \
    --PersonExDescriptionInfos.1.PersonExDescription 'AI Product Center' \
    --PersonExDescriptionInfos.2.PersonExDescriptionIndex 2 \
    --PersonExDescriptionInfos.2.PersonExDescription 'Face Recognition Product Team'
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

**Example 3: Sample error**

The person ID must be unique.

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
            "Message": "The person ID already exists. It must be unique."
        },
        "RequestId": "76dedef7-af27-4a20-9064-c5ef3133926d"
    }
}
```

**Example 4: Sample error - 2**

The group ID does not exist.

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
            "Message": "The group ID does not exist."
        },
        "RequestId": "dfa512fc-fd07-4bf1-a292-cb497b620857"
    }
}
```

