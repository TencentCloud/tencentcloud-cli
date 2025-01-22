**Example 1: 修改用户绑定的资源组**



Input: 

```
tccli cdwdoris ModifyUserBindWorkloadGroup --cli-unfold-argument  \
    --InstanceId cdwdoris-qliqegj3 \
    --BindUsers.0.UserName admin \
    --BindUsers.0.Host % \
    --BindUsers.1.UserName cuser \
    --BindUsers.1.Host 127.0.0.1 \
    --OldWorkloadGroupName group1 \
    --NewWorkloadGroupName newgroup
```

Output: 
```
{
    "Response": {
        "ErrorMsg": "",
        "RequestId": "117ad1ab-8571-4085-8356-382b6a5f07f6"
    }
}
```

