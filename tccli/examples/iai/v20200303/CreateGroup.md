**Example 1: Creating group**



Input: 

```
tccli iai CreateGroup --cli-unfold-argument  \
    --GroupName 'Tencent Employees in Shenzhen' \
    --FaceModelVersion 3.0 \
    --GroupId TencentShenZhenEmployee \
    --Tag 'Excluding interns' \
    --GroupExDescriptions Division 'Department name' 'Team name'
```

Output: 
```
{
    "Response": {
        "FaceModelVersion": "3.0",
        "RequestId": "e53ee4ec-9099-4b35-a129-21dd4820ff85"
    }
}
```

**Example 2: Creating group - 2**



Input: 

```
tccli iai CreateGroup --cli-unfold-argument  \
    --GroupName 'Dormitory Building #1, Zhuyuan Campus, XX University' \
    --GroupId ZhuYuanDormitoryNo1 \
    --FaceModelVersion 3.0 \
    --Tag 'All girls' \
    --GroupExDescriptions 'School name' Major Grade 'Student ID'
```

Output: 
```
{
    "Response": {
        "FaceModelVersion": "3.0",
        "RequestId": "1695f3dd-b668-479e-8b87-f37de371a8ec"
    }
}
```

**Example 3: Sample error**

The group ID must be unique.

Input: 

```
tccli iai CreateGroup --cli-unfold-argument  \
    --GroupName 'Tencent Employees in Shenzhen' \
    --GroupId TencentShenZhenEmployee
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "InvalidParameterValue.GroupIdAlreadyExist",
            "Message": "The group ID already exists. It must be unique."
        },
        "RequestId": "76ec6e41-37d6-4ab9-abef-48ef0c6ab175"
    }
}
```

**Example 4: Sample error - 2**

The group ID cannot contain Chinese characters.

Input: 

```
tccli iai CreateGroup --cli-unfold-argument  \
    --GroupName 'Tencent Employees in Shenzhen' \
    --GroupId 'Tencent Employees in Shenzhen'
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "InvalidParameterValue.GroupIdIllegal",
            "Message": "The group ID contains invalid characters. It can contain only letters, digits, and -%@#&_."
        },
        "RequestId": "8125dda4-2905-4e02-88bd-79a93a660ad2"
    }
}
```

