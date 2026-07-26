**Example 1: 批量重置用户密码**



Input: 

```
tccli tdmysql ResetUsersPassword --cli-unfold-argument  \
    --InstanceId tdsql3-831053d8 \
    --Users.0.UserName test1 \
    --Users.0.Host % \
    --Users.0.Password tdstore@123
```

Output: 
```
{
    "Response": {
        "FlowId": 4295045724,
        "RequestId": "76fc6e35-0f49-40e5-90f2-2cc165841df7"
    }
}
```

