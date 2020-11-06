**Example 1: Getting person list**

This example shows you how to get the list of persons in a specified group.

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
                    "School of Computing",
                    "Software Engineering",
                    "'15",
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

**Example 2: Getting person list - 2**



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
                    "Cloud and Smart Industries Group",
                    "Big Data and AI Product Center",
                    "Face Recognition Product Team"
                ],
                "FaceIds": [
                    "2877242150180891493"
                ],
                "CreationTimestamp": 1594642823572
            }
        ],
        "PersonNum": 1,
        "FaceNum": 1,
        "FaceModelVersion": "3.0",
        "RequestId": "aa292f16-27d9-423b-9048-cdd43f6e4156"
    }
}
```

**Example 3: Sample error**



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
            "Message": "The group ID does not exist."
        },
        "RequestId": "b7c0cd81-d621-465f-8fd6-86a6b49e67be"
    }
}
```

