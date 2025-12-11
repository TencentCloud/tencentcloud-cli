**Example 1: 创建连通性检测任务**

创建连通性检测任务

Input: 

```
tccli dbs CreateConnectTestJob --cli-unfold-argument  \
    --Endpoint.DatabaseType mysql \
    --Endpoint.AccessType ccn \
    --Endpoint.UserName user1 \
    --Endpoint.Password qwer1234 \
    --Endpoint.Region ap-guangzhou \
    --Endpoint.Supplier others
```

Output: 
```
{
    "Response": {
        "ConnTaskId": "task-asdqerq",
        "RequestId": "196f3f7d-ca09-4b1b-8bd8-62ef48cfe791"
    }
}
```

