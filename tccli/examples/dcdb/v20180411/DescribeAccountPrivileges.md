**Example 1: 查询云数据库账号全局权限**



Input: 

```
tccli dcdb DescribeAccountPrivileges --cli-unfold-argument  \
    --InstanceId dcdbt-fdpjf5zh \
    --UserName testuser1 \
    --Host 172.17.% \
    --DbName * \
    --Type *
```

Output: 
```
{
    "Response": {
        "RequestId": "3381c9e9-d87f-4e21-ba1d-596d6f697a7e",
        "InstanceId": "dcdbt-fdpjf5zh",
        "UserName": "testuser1",
        "Host": "172.17.%",
        "Privileges": [
            "SELECT",
            "UPDATE"
        ]
    }
}
```

