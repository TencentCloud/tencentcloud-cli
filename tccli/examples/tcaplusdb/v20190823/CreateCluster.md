**Example 1: 创建集群Cluster**

新创建TcaplusDB集群

Input: 

```
tccli tcaplusdb CreateCluster --cli-unfold-argument  \
    --IdlType TDR \
    --ClusterName gz测试TDR \
    --VpcId vpc-kppg4pm1 \
    --SubnetId subnet-3sww53pa \
    --Password 84ea4cbf06573ED
```

Output: 
```
{
    "Response": {
        "ClusterId": "6179109757",
        "RequestId": "8f1cc454-4a80-4ed3-a6c3-b7df2b0e8ec7"
    }
}
```

