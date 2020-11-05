**Example 1: Modifying the password of a TencentDB account**



Input: 

```
tccli dcdb ResetAccountPassword --cli-unfold-argument  \
    --InstanceId dcdbt-fdpjf5zh\
    --UserName testuser1\
    --Host 172.17.%\
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

