**Example 1: Calling the GetGroupList API**

This example shows you how to get the group list.

Input: 

```
tccli iai GetGroupList --cli-unfold-argument  \
    --Offset 0\
    --Limit 10
```

Output: 
```
{
    "Response": {
        "GroupInfos": [
            {
                "GroupName": "Tencent Shenzhen Employees",
                "GroupId": "TencentShenZhenEmployee",
                "GroupExDescriptions": [
                    "Business group",
                    "Department name",
                    "Group name"
                ],
                "Tag": "Excluding interns"
                "FaceModelVersion":"3.0",
                "CreationTimestamp": 1592210245686
            },
            {
                "GroupName": "Building 1, Zhuyuan Dormitory of XXX University",
                "GroupId": "ZhuYuanDormitoryNo1",
                "GroupExDescriptions": [
                    "School name",
                    "Major",
                    "Grade",
                    "Student ID"
                ],
                "Tag": "Female only"
                "FaceModelVersion": "3.0",
                "CreationTimestamp": 1594552117118
            }
        ],
        "GroupNum": 2,
        "RequestId": "72102087-a18d-4225-9ae9-87ef49e9f63e"
    }
}
```

**Example 2: Sample Error**

This example shows the error occurred when the starting number is less than 0.

Input: 

```
tccli iai GetGroupList --cli-unfold-argument  \
    --Offset -1\
    --Limit 100
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "InvalidParameter",
            "Message": "The value type of parameter `Offset` is not valid."
        },
        "RequestId": "9c987f11-f5d0-4aa7-aa13-3d8c1b4b3042"
    }
}
```

**Example 3: Sample Error 2**

This example shows the error occurred when the number of returned results is greater than 1000.

Input: 

```
tccli iai GetGroupList --cli-unfold-argument  \
    --Offset 0\
    --Limit 1001
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "InvalidParameterValue.LimitExceed",
            "Message": "Number of returned results exceeded the limit."
        },
        "RequestId": "a6bb57de-773b-45e4-9e1c-c30ef48eba85"
    }
}
```

