**Example 1: 修改用户Hba**

修改用户Hba

Input: 

```
tccli cdwpg ModifyUserHba --cli-unfold-argument  \
    --InstanceId cdwpg-abc \
    --HbaConfigs.0.Type 1abc \
    --HbaConfigs.0.Database 1abc \
    --HbaConfigs.0.User 1abc \
    --HbaConfigs.0.Address 1abc \
    --HbaConfigs.0.Mask 1abc \
    --HbaConfigs.0.Method 1abc
```

Output: 
```
{
    "Response": {
        "TaskId": 0,
        "ErrorMsg": "",
        "RequestId": "1abc"
    }
}
```

