**Example 1: 克隆集群**



Input: 

```
tccli tdcpg CloneClusterToPointInTime --cli-unfold-argument  \
    --InstanceCount 1 \
    --AutoRenewFlag 0 \
    --Zone ap-guangzhou-3 \
    --ClusterName MyClusterName \
    --DBVersion 10.17 \
    --Period 12 \
    --CPU 1 \
    --PayMode PREPAID \
    --VpcId vpc-xxxx \
    --Memory 2 \
    --SubnetId subnet-xxxx \
    --Port 5432 \
    --SourceClusterId tdcpg-xx \
    --SourceDataPoint 2021-11-18T18:10:25+08:00
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

