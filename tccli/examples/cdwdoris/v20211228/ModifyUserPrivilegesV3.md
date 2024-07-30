**Example 1: 设置全局catalog权限**



Input: 

```
tccli cdwdoris ModifyUserPrivilegesV3 --cli-unfold-argument  \
    --InstanceId cdwdoris-xx \
    --UserName test \
    --UserPrivileges.IsSetGlobalCatalog True
```

Output: 
```
{
    "Response": {
        "ErrorMsg": "abc",
        "InstanceId": "abc",
        "RequestId": "abc"
    }
}
```

