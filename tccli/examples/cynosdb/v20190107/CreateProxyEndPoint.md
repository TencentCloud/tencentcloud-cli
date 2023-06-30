**Example 1: 创建数据库代理连接点**

创建数据库代理连接点

Input: 

```
tccli cynosdb CreateProxyEndPoint --cli-unfold-argument  \
    --ClusterId abc \
    --UniqueVpcId abc \
    --UniqueSubnetId abc \
    --ConnectionPoolType abc \
    --OpenConnectionPool abc \
    --ConnectionPoolTimeOut 0 \
    --SecurityGroupIds abc \
    --Description abc \
    --Vip abc \
    --WeightMode abc \
    --AutoAddRo abc \
    --FailOver abc \
    --ConsistencyType abc \
    --RwType abc \
    --ConsistencyTimeOut 0 \
    --TransSplit True \
    --AccessMode abc \
    --InstanceWeights.0.InstanceId abc \
    --InstanceWeights.0.Weight 0
```

Output: 
```
{
    "Response": {
        "FlowId": 0,
        "TaskId": 0,
        "ProxyGroupId": "abc",
        "RequestId": "abc"
    }
}
```

