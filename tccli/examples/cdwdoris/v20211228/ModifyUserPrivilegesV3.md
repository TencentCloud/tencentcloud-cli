**Example 1: 设置全局catalog权限**



Input: 

```
tccli cdwdoris ModifyUserPrivilegesV3 --cli-unfold-argument  \
    --InstanceId cdwdoris-qliqegj3 \
    --UserName user \
    --UserPrivileges.IsSetGlobalCatalog True
```

Output: 
```
{
    "Response": {
        "ErrorMsg": "",
        "InstanceId": "cdwdoris-qliqegj3",
        "RequestId": "117ad1ab-8571-4085-8356-382b6a5f07f6"
    }
}
```

