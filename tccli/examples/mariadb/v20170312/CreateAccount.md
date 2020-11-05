**Example 1: Creating TencentDB instance access account**



Input: 

```
tccli mariadb CreateAccount --cli-unfold-argument  \
    --InstanceId tdsql-fdpjf5zh\
    --UserName testuser1\
    --Host 172.17.%\
    --Password 1234qweri#\
    --Description 'Test account'
```

Output: 
```
{
    "Response": {
        "RequestId": "2cc4e4dc-c3e9-4858-ab80-03e3526cf24d",
        "InstanceId": "tdsql-fdpjf5zh",
        "UserName": "testuser1",
        "Host": "172.17.%",
        "Readonly": 0
    }
}
```

