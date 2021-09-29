**Example 1: 绑定工作组到用户**



Input: 

```
tccli dlc BindWorkGroupsToUser --cli-unfold-argument  \
    --AddInfo.UserId 10003237654 \
    --AddInfo.WorkGroupIds 112
```

Output: 
```
{
    "Response": {
        "RequestId": "27633f02-4b56-4963-91a4-7fabe4b82cba"
    }
}
```

