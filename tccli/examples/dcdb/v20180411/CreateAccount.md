**Example 1: Create an Access account for a cloud database instance**



Input: 

```
tccli dcdb CreateAccount --cli-unfold-argument  \
    --InstanceId dcdbt-fdpjf5zh\
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
        "CdbInstanceId": "dcdbt-fdpjf5zh",
        "UserName": "testuser1",
        "Host": "172.17.%",
        "Readonly": 0
    }
}
```

