**Example 1: 创建数据库**



Input: 

```
tccli cynosdb CreateClusterDatabase --cli-unfold-argument  \
    --UserHostPrivileges.0.DbUserName root \
    --UserHostPrivileges.0.DbHost % \
    --UserHostPrivileges.0.DbPrivilege xx \
    --CollateRule utf8_general_ci \
    --DbName test \
    --Description test-beizhu \
    --CharacterSet utf8 \
    --ClusterId cynosdbmysql-xxxxxx
```

Output: 
```
{
    "Response": {
        "RequestId": "f569bea2-0a51-11ec-af61-525400542aa6"
    }
}
```

