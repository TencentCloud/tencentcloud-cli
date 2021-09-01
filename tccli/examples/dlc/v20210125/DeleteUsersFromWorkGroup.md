**Example 1: 从工作组中删除用户**



Input: 

```
tccli dlc DeleteUsersFromWorkGroup --cli-unfold-argument  \
    --AddInfo.WorkGroupId 0 \
    --AddInfo.UserIds xx
```

Output: 
```
{
    "Response": {
        "RequestId": "xx"
    }
}
```

