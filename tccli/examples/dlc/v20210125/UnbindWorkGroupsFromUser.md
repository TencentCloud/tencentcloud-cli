**Example 1: 解绑用户上的用户组**



Input: 

```
tccli dlc UnbindWorkGroupsFromUser --cli-unfold-argument  \
    --AddInfo.UserId xx \
    --AddInfo.WorkGroupIds 0
```

Output: 
```
{
    "Response": {
        "RequestId": "xx"
    }
}
```

