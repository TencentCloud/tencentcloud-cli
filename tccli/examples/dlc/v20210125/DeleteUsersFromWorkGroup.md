**Example 1: 从工作组中删除用户**



Input: 

```
tccli dlc DeleteUsersFromWorkGroup --cli-unfold-argument  \
    --AddInfo.WorkGroupId 112 \
    --AddInfo.UserIds 10003237654
```

Output: 
```
{
    "Response": {
        "RequestId": "1fd1d314-00e1-421b-9838-6e6b6c9c5419"
    }
}
```

