**Example 1: test**



Input: 

```
tccli emr AddUsersForUserManager --cli-unfold-argument  \
    --InstanceId xx \
    --UserManagerUserList.0.UserName test1 \
    --UserManagerUserList.0.UserGroup test1 \
    --UserManagerUserList.0.PassWord test1 \
    --UserManagerUserList.0.ReMark test1 \
    --UserManagerUserList.1.UserName test2 \
    --UserManagerUserList.1.UserGroup test2 \
    --UserManagerUserList.1.PassWord test2 \
    --UserManagerUserList.1.ReMark test2 \
    --UserManagerUserList.2.UserName test3 \
    --UserManagerUserList.2.UserGroup test3 \
    --UserManagerUserList.2.PassWord test3 \
    --UserManagerUserList.2.ReMark test3 \
    --UserManagerUserList.3.UserName test4 \
    --UserManagerUserList.3.UserGroup test4 \
    --UserManagerUserList.3.PassWord test4 \
    --UserManagerUserList.3.ReMark test4
```

Output: 
```
{
    "Response": {
        "FailedUserList": [],
        "RequestId": "782d3570-9f82-4bff-974a-17cf684fdfe9",
        "SuccessUserList": [
            "test1",
            "test2",
            "test3",
            "test4"
        ]
    }
}
```

