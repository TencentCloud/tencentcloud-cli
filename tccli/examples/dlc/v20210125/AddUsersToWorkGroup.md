**Example 1: 添加用户到工作组**



Input: 

```
tccli dlc AddUsersToWorkGroup --cli-unfold-argument  \
    --AddInfo.WorkGroupId 122 \
    --AddInfo.UserIds 10003237654
```

Output: 
```
{
    "Response": {
        "RequestId": "c8900a05-8939-4b47-a3ab-3f3e92e439b7"
    }
}
```

