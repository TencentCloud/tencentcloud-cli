**Example 1: 创建 DB Custom 集群**



Input: 

```
tccli dbdc CreateDBCustomCluster --cli-unfold-argument  \
    --ContainerNetwork.VpcId vpc-evvog2gd \
    --ContainerNetwork.SubnetIds subnet-clk8il4i \
    --ClusterName 生产集群-001 \
    --ApiServerNetwork.VpcId vpc-evvog2gd \
    --ApiServerNetwork.SubnetId subnet-clk8il4i \
    --ClusterDescription L500 \
    --Tags.0.Key 环境 \
    --Tags.0.Value 生产 \
    --ClientToken a8800d2e-db3e-41bb-8e49-f71fd8314047
```

Output: 
```
{
    "Response": {
        "ClusterId": "dbcc-1p6xo1xz",
        "TaskId": 80,
        "RequestId": "95a44313-4cd0-436f-a9c1-99b449896ce6"
    }
}
```

