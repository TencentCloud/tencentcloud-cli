**Example 1: 创建cdc-ckafka共享集群**



Input: 

```
tccli ckafka CreateCdcCluster --cli-unfold-argument  \
    --CdcId cluster-d8htgb6k \
    --CdcVpcId vpc-ixenz42t \
    --CdcSubnetId subnet-k8x1dviw \
    --ZoneId 100002 \
    --Bandwidth 1200 \
    --DiskSize 800 \
    --DiskType CLOUD_SSD \
    --SystemDiskType CLOUD_SSD
```

Output: 
```
{
    "Response": {
        "Result": {
            "TaskId": 1111
        },
        "RequestId": "20e995ed-75b9-43bb-84c0-35676567e1a8"
    }
}
```

