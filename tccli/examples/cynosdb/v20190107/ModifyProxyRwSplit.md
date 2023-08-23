**Example 1: 配置数据库代理读写分离**

配置数据库代理读写分离

Input: 

```
tccli cynosdb ModifyProxyRwSplit --cli-unfold-argument  \
    --ClusterId cynosdbmysql-asd \
    --ProxyGroupId cynosdbmysql-proxy-qwe \
    --ConsistencyType eventual \
    --ConsistencyTimeOut 10 \
    --WeightMode system \
    --InstanceWeights.0.InstanceId cynosdbmysql-ins-qwe \
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
        "FlowId": 0,
        "TaskId": 0,
        "RequestId": "abc"
    }
}
```

