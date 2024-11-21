**Example 1: 创建数据库代理**

创建数据库代理

Input: 

```
tccli cynosdb CreateProxy --cli-unfold-argument  \
    --ClusterId cynosdbmysql-mwg7212w \
    --UniqueVpcId vpc-4pbgo2lk \
    --UniqueSubnetId subnet-a2emqn1t \
    --ProxyCount 2 \
    --Cpu 2 \
    --Mem 4000 \
    --ConnectionPoolType SessionConnectionPool \
    --OpenConnectionPool yes \
    --ConnectionPoolTimeOut 0 \
    --SecurityGroupIds sg-qwaszx \
    --Description Fill in the description \
    --ProxyZones.0.ProxyNodeZone ap-beijing-6 \
    --ProxyZones.0.ProxyNodeCount 2
```

Output: 
```
{
    "Response": {
        "FlowId": 358874,
        "TaskId": 1063084,
        "RequestId": "a88257ed-174e-499c-b390-dc535e664b94"
    }
}
```

