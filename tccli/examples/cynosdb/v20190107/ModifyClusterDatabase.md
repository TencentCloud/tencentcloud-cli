**Example 1: 创建数据库**



Input: 

```
tccli cynosdb ModifyClusterDatabase --cli-unfold-argument  \
    --OldUserHostPrivileges.0.DbUserName test \
    --OldUserHostPrivileges.0.DbHost 1.1.1.1 \
    --OldUserHostPrivileges.0.DbPrivilege create \
    --NewUserHostPrivileges.0.DbUserName test \
    --NewUserHostPrivileges.0.DbHost 1.1.11.1 \
    --NewUserHostPrivileges.0.DbPrivilege delete \
    --ClusterId cynosdbmysql-asd \
    --DbName testDb \
    --Description this is a dbtable
```

Output: 
```
{
    "Response": {
        "RequestId": "f569bea2-0a51-11ec-af61-525400542aa6"
    }
}
```

