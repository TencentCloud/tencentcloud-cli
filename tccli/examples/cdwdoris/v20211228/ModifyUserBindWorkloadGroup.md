**Example 1: 修改用户绑定的资源组**



Input: 

```
tccli cdwdoris ModifyUserBindWorkloadGroup --cli-unfold-argument  \
    --InstanceId abc \
    --BindUsers.0.UserName test \
    --BindUsers.0.Host % \
    --BindUsers.1.UserName test \
    --BindUsers.1.Host 127.0.0.1 \
    --OldWorkloadGroupName abc \
    --NewWorkloadGroupName abc1
```

Output: 
```
{
    "Response": {
        "ErrorMsg": "abc",
        "RequestId": "abc"
    }
}
```

