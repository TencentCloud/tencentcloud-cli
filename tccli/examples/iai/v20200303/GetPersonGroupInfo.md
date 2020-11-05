**Example 1: Getting the group information of person**



Input: 

```
tccli iai GetPersonGroupInfo --cli-unfold-argument  \
    --PersonId 2001\
    --Offset 0\
    --Limit 10
```

Output: 
```
{
    "Response": {
        "GroupNum": "1",
        "PersonGroupInfos": [
            {
                "GroupId": "ZhuYuanDormitoryNo1",
                "PersonExDescriptions": [
                    "School of Computing",
                    "Software Engineering",
                    "'15",
                    "3150108080"
                ]
            }
        ],
        "FaceModelVersion": "3.0",
        "RequestId": "671f0a1d-2b35-47c4-b9d1-b18053f71a04"
    }
}
```

**Example 2: Getting the group information of person - 2**



Input: 

```
tccli iai GetPersonGroupInfo --cli-unfold-argument  \
    --PersonId 1001\
    --Offset 0\
    --Limit 10
```

Output: 
```
{
    "Response": {
        "GroupNum": "1",
        "PersonGroupInfos": [
            {
                "GroupId": "TencentShenZhenEmployee",
                "PersonExDescriptions": [
                    "Cloud and Smart Industries Group",
                    "Big Data and AI Product Center",
                    "Face Recognition Product Team"
                ]
            }
        ],
        "FaceModelVersion": "3.0",
        "RequestId": "b7a505ad-4a85-42da-97b3-886c7999fb76"
    }
}
```

**Example 3: Sample error**

The person ID does not exist.

Input: 

```
tccli iai GetPersonGroupInfo --cli-unfold-argument  \
    --PersonId 1002\
    --Offset 0\
    --Limit 10
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "InvalidParameterValue.PersonIdNotExist",
            "Message": "The person ID does not exist."
        },
        "RequestId": "98330f25-eb2e-432a-a30c-3830774210c1"
    }
}
```

