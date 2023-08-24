**Example 1: 创建数据库代理连接点**

创建数据库代理连接点

Input: 

```
tccli cynosdb CreateProxyEndPoint --cli-unfold-argument  \
    --ClusterId cynosdbmysql-asd \
    --UniqueVpcId vpc-azx \
    --UniqueSubnetId subnet-qwe \
    --ConnectionPoolType SessionConnectionPool \
    --OpenConnectionPool yes \
    --ConnectionPoolTimeOut 0 \
    --SecurityGroupIds sg-dtwhs6 \
    --Description abc \
    --Vip 1.1.1.1 \
    --WeightMode system \
    --AutoAddRo yes \
    --FailOver  \
    --ConsistencyType eventual \
    --RwType READWRITE \
    --ConsistencyTimeOut 0 \
    --TransSplit True \
    --AccessMode nearby \
    --InstanceWeights.0.InstanceId cynosdbmysql-ins-qwe \
    --InstanceWeights.0.Weight 0
```

Output: 
```
{
    "Response": {
        "FlowId": 0,
        "TaskId": 0,
        "ProxyGroupId": "cynosdbmysql-proxy-asd",
        "RequestId": "abc"
    }
}
```

