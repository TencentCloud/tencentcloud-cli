**Example 1: 创建数据库代理连接点**

创建数据库代理连接点

Input: 

```
tccli cynosdb CreateProxyEndPoint --cli-unfold-argument  \
    --ClusterId cynosdbmysql-dnofdr2d \
    --UniqueVpcId vpc-azx \
    --UniqueSubnetId subnet-qwe \
    --ConnectionPoolType SessionConnectionPool \
    --OpenConnectionPool yes \
    --ConnectionPoolTimeOut 0 \
    --SecurityGroupIds sg-dtwhs6 \
    --Description tomnode1 \
    --Vip 1.1.1.1 \
    --WeightMode system \
    --AutoAddRo yes \
    --FailOver  \
    --ConsistencyType eventual \
    --RwType READWRITE \
    --ConsistencyTimeOut 0 \
    --TransSplit True \
    --AccessMode nearby \
    --InstanceWeights.0.InstanceId cynosdbmysql-ins-c2twj0qf \
    --InstanceWeights.0.Weight 0
```

Output: 
```
{
    "Response": {
        "FlowId": 146737,
        "TaskId": 187463,
        "ProxyGroupId": "cynosdbmysql-proxy-4378e0kd",
        "RequestId": "a5706353-296a-4992-ad07-ac4a48eeba43"
    }
}
```

