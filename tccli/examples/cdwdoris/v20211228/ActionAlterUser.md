**Example 1: 新增、修改ck集群用户**



Input: 

```
tccli cdwdoris ActionAlterUser --cli-unfold-argument  \
    --UserInfo.InstanceId abc \
    --UserInfo.UserName abc \
    --UserInfo.PassWord abc \
    --UserInfo.WhiteHost abc \
    --UserInfo.OldWhiteHost abc \
    --UserInfo.Describe abc \
    --UserInfo.OldPwd abc \
    --ApiType abc \
    --UserPrivilege 0
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

