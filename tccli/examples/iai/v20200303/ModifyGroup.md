**Example 1: Modifying group**

This example shows you how to modify the name, tag, and custom description field of a group.

Input: 

```
tccli iai ModifyGroup --cli-unfold-argument  \
    --GroupId ZhuYuanDormitoryNo1\
    --GroupName 'Building Dormitory #1, Zhuyuan Campus, XX University'\
    --Tag Graduates\
    --GroupExDescriptionInfos.0.GroupExDescriptionIndex 0\
    --GroupExDescriptionInfos.0.GroupExDescription School
```

Output: 
```
{
    "Response": {
        "RequestId": "da051f16-0400-49d4-9832-2cfd3b51866f"
    }
}
```

**Example 2: Modifying group - 2**

This example shows you how to modify the name, tag, and custom description field of a group.

Input: 

```
tccli iai ModifyGroup --cli-unfold-argument  \
    --GroupId TencentShenZhenEmployee\
    --GroupName 'Current Tencent Employees in Shenzhen'\
    --Tag 'Including interns'\
    --GroupExDescriptionInfos.0.GroupExDescriptionIndex 1\
    --GroupExDescriptionInfos.0.GroupExDescription Department\
    --GroupExDescriptionInfos.1.GroupExDescriptionIndex 2\
    --GroupExDescriptionInfos.1.GroupExDescription 'Project team'
```

Output: 
```
{
    "Response": {
        "RequestId": "98381738-509f-4749-8a66-dbf54247333d"
    }
}
```

**Example 3: Sample error**



Input: 

```
tccli iai ModifyGroup --cli-unfold-argument  \
    --GroupId TencentShenZhenEmployee\
    --GroupExDescriptionInfos.0.GroupExDescriptionIndex 0\
    --GroupExDescriptionInfos.0.GroupExDescription Department
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "FailedOperation.DuplicatedGroupDescription",
            "Message": "The custom description field must be unique in the group."
        },
        "RequestId": "4b483679-3f08-4a7c-b827-4a6332dc030f"
    }
}
```

**Example 4: Sample error - 2**

The group name must be unique.

Input: 

```
tccli iai ModifyGroup --cli-unfold-argument  \
    --GroupId TencentShenZhenEmployee\
    --GroupName 'Building Dormitory #1, Zhuyuan Campus, XX University'
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "InvalidParameterValue.GroupNameAlreadyExist",
            "Message": "The group name already exists. It must be unique."
        },
        "RequestId": "2dcce170-30cf-4078-9b3c-309362fbad21"
    }
}
```

