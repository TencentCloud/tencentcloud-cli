**Example 1: 配置数据库代理读写分离**

配置数据库代理读写分离

Input: 

```
tccli cynosdb ModifyProxyRwSplit --cli-unfold-argument  \
    --ClusterId abc \
    --ProxyGroupId abc \
    --ConsistencyType abc \
    --ConsistencyTimeOut abc \
    --WeightMode abc \
    --InstanceWeights.0.InstanceId abc \
    --InstanceWeights.0.Weight 0 \
    --FailOver abc \
    --AutoAddRo abc \
    --OpenRw abc \
    --RwType abc \
    --TransSplit True \
    --AccessMode abc \
    --OpenConnectionPool abc \
    --ConnectionPoolType abc \
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

