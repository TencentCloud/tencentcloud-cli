**Example 1: 配置数据库代理读写分离**

配置数据库代理读写分离

Input: 

```
tccli cynosdb ModifyProxyRwSplit --cli-unfold-argument  \
    --ClusterId cynosdbmysql-dnofdr2d \
    --ProxyGroupId cynosdbmysql-proxy-4378e0kd \
    --ConsistencyType eventual \
    --ConsistencyTimeOut 10 \
    --WeightMode system \
    --InstanceWeights.0.InstanceId cynosdbmysql-ins-c2twj0qf \
    --InstanceWeights.0.Weight 0 \
    --FailOver  \
    --AutoAddRo yes \
    --OpenRw yes \
    --RwType READONLY \
    --TransSplit True \
    --AccessMode nearby \
    --OpenConnectionPool yes \
    --ConnectionPoolType SessionConnectionPool \
    --ConnectionPoolTimeOut 0
```

Output: 
```
{
    "Response": {
        "FlowId": 134762,
        "TaskId": 146783,
        "RequestId": "a5706353-296a-4992-ad07-ac4a48eeba43"
    }
}
```

