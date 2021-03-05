**Example 1: 修改云数据库账号的密码**



Input: 

```
tccli mariadb ResetAccountPassword --cli-unfold-argument  \
    --InstanceId tdsql-fdpjf5zh \
    --UserName testuser1 \
    --Host 172.17.% \
    --Password abcd8765_.
```

Output: 
```
{
    "Response": {
        "RequestId": "c7b1680d-db03-4f20-8684-a865ce7bcd38"
    }
}
```

