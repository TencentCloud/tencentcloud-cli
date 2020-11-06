**Example 1: Modifying TencentDB account remarks**



Input: 

```
tccli mariadb ModifyAccountDescription --cli-unfold-argument  \
    --InstanceId tdsql-fdpjf5zh \
    --UserName testuser1 \
    --Host 172.17.% \
    --Description 'Test account'
```

Output: 
```
{
    "Response": {
        "RequestId": "aef9be24-4d49-4358-8022-3405a361fd3b"
    }
}
```

