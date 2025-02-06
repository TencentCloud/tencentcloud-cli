**Example 1: 新增、修改ck集群用户**



Input: 

```
tccli cdwdoris ActionAlterUser --cli-unfold-argument  \
    --UserInfo.InstanceId cdwdoris-xasdf \
    --UserInfo.UserName user \
    --UserInfo.PassWord pwd \
    --UserInfo.WhiteHost host \
    --UserInfo.OldWhiteHost o_host \
    --UserInfo.Describe describe \
    --UserInfo.OldPwd pwd \
    --ApiType type \
    --UserPrivilege 3
```

Output: 
```
{
    "Response": {
        "ErrorMsg": "err",
        "RequestId": "xawef0-asxca"
    }
}
```

