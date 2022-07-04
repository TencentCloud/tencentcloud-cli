**Example 1: 为云数据库实例创建访问账号**



Input: 

```
tccli mariadb CreateAccount --cli-unfold-argument  \
    --UserName testuser1 \
    --Description 测试帐号 \
    --InstanceId tdsql-fdpjf5zh \
    --ReadOnly 0 \
    --Host 172.17.% \
    --Password 1234qweri#
```

Output: 
```
{
    "Response": {
        "RequestId": "2cc4e4dc-c3e9-4858-ab80-03e3526cf24d",
        "InstanceId": "tdsql-fdpjf5zh",
        "UserName": "testuser1",
        "Host": "172.17.%",
        "ReadOnly": 0
    }
}
```

