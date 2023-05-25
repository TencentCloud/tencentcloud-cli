**Example 1: 创建数据库**



Input: 

```
tccli cynosdb ModifyClusterDatabase --cli-unfold-argument  \
    --OldUserHostPrivileges.0.DbUserName xx \
    --OldUserHostPrivileges.0.DbHost xx \
    --OldUserHostPrivileges.0.DbPrivilege xx \
    --NewUserHostPrivileges.0.DbUserName xx \
    --NewUserHostPrivileges.0.DbHost xx \
    --NewUserHostPrivileges.0.DbPrivilege xx \
    --ClusterId xx \
    --DbName xx \
    --Description xx
```

Output: 
```
{
    "Response": {
        "RequestId": "f569bea2-0a51-11ec-af61-525400542aa6"
    }
}
```

