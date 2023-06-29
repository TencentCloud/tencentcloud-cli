**Example 1: 创建集群**



Input: 

```
tccli tdcpg CreateCluster --cli-unfold-argument  \
    --InstanceCount 1 \
    --AutoRenewFlag 0 \
    --Zone ap-guangzhou-3 \
    --ClusterName MyClusterName \
    --ProjectId 0 \
    --DBVersion 10.17 \
    --Period 12 \
    --MasterUserPassword 111@abc \
    --CPU 1 \
    --PayMode PREPAID \
    --VpcId vpc-xxxx \
    --Memory 2 \
    --SubnetId subnet-xxxx \
    --Port 5432
```

Output: 
```
{
    "Response": {
        "DealNameSet": [
            "20211028111234680033121"
        ],
        "RequestId": "03ea3f94-297d-11eb-8f30-525400b7dd5a"
    }
}
```

