**Example 1: 重新添加用户列表**



Input: 

```
tccli emr AddUsersAgainForUserManager --cli-unfold-argument  \
    --InstanceId emr-xxx \
    --Users hadoop
```

Output: 
```
{
    "Response": {
        "SuccessUserList": [
            "hadoop"
        ],
        "FailedUserList": [],
        "RequestId": "abc"
    }
}
```

