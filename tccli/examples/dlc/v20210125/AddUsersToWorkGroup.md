**Example 1: 添加用户到工作组**



Input: 

```
tccli dlc AddUsersToWorkGroup --cli-unfold-argument  \
    --AddInfo.WorkGroupId 0 \
    --AddInfo.UserIds xx
```

Output: 
```
{
    "Response": {
        "RequestId": "xxx"
    }
}
```

