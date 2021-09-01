**Example 1: 绑定工作组到用户**



Input: 

```
tccli dlc BindWorkGroupsToUser --cli-unfold-argument  \
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

