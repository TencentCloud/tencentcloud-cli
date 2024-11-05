**Example 1: 创建数据库**

创建数据库

Input: 

```
tccli cynosdb CreateClusterDatabase --cli-unfold-argument  \
    --ClusterId cynosdbmysql-mwg712en \
    --DbName tom \
    --CharacterSet utf8 \
    --CollateRule utf8_general_ci \
    --UserHostPrivileges.0.DbUserName root \
    --UserHostPrivileges.0.DbHost 172.1.1.1 \
    --UserHostPrivileges.0.DbPrivilege DDL \
    --Description tomuse
```

Output: 
```
{
    "Response": {
        "RequestId": "f569bea2-0a51-11ec-af61-525400542aa6"
    }
}
```

