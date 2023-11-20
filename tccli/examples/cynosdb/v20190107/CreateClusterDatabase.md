**Example 1: 创建数据库**

创建数据库

Input: 

```
tccli cynosdb CreateClusterDatabase --cli-unfold-argument  \
    --ClusterId abc \
    --DbName abc \
    --CharacterSet abc \
    --CollateRule abc \
    --UserHostPrivileges.0.DbUserName abc \
    --UserHostPrivileges.0.DbHost abc \
    --UserHostPrivileges.0.DbPrivilege abc \
    --Description abc
```

Output: 
```
{
    "Response": {
        "RequestId": "f569bea2-0a51-11ec-af61-525400542aa6"
    }
}
```

