**Example 1: 创建数据库代理**

创建数据库代理

Input: 

```
tccli cynosdb CreateProxy --cli-unfold-argument  \
    --ClusterId abc \
    --UniqueVpcId abc \
    --UniqueSubnetId abc \
    --ProxyCount 0 \
    --Cpu 0 \
    --Mem 0 \
    --ConnectionPoolType abc \
    --OpenConnectionPool abc \
    --ConnectionPoolTimeOut 0 \
    --SecurityGroupIds abc \
    --Description abc \
    --ProxyZones.0.ProxyNodeZone abc \
    --ProxyZones.0.ProxyNodeCount 0
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

