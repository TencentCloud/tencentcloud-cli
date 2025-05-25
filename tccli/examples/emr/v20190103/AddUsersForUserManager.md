**Example 1: 新增用户**



Input: 

```
tccli emr AddUsersForUserManager --cli-unfold-argument  \
    --InstanceId emr-o88f3whr \
    --UserManagerUserList.0.UserName user1 \
    --UserManagerUserList.0.UserGroup group1 \
    --UserManagerUserList.0.PassWord ceshi123 \
    --UserManagerUserList.0.ReMark ceshi \
    --UserManagerUserList.0.Groups group1
```

Output: 
```
{
    "Response": {
        "FailedUserList": [],
        "RequestId": "69048737-8f4f-4825-b4f6-a67dbf3f198c",
        "SuccessUserList": [
            "user1"
        ]
    }
}
```

