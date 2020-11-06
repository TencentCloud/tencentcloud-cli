**Example 1: 修改云数据库账号备注**



Input: 

```
tccli dcdb ModifyAccountDescription --cli-unfold-argument  \
    --InstanceId dcdbt-fdpjf5zh \
    --UserName testuser1 \
    --Host 172.17.% \
    --Description 用于测试的账号
```

Output: 
```
{
    "Response": {
        "RequestId": "aef9be24-4d49-4358-8022-3405a361fd3b"
    }
}
```

