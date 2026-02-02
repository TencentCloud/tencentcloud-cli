**Example 1: 新建 TDSQL-C 分析集群**

用于新建一个 TDSQL-C 分析集群

Input: 

```
tccli cynosdb CreateLibraDBClusters --cli-unfold-argument  \
    --Count 1 \
    --Zone ap-guangzhou-7 \
    --InstanceInitInfos.0.Cpu 4 \
    --InstanceInitInfos.0.Memory 16 \
    --InstanceInitInfos.0.StorageSize 20 \
    --InstanceInitInfos.0.StorageType  \
    --InstanceInitInfos.0.InstanceType Common \
    --InstanceInitInfos.0.LibraDBVersion  \
    --InstanceInitInfos.0.InstanceCount 1 \
    --InstanceInitInfos.0.VpcId vpc-nnakli31 \
    --InstanceInitInfos.0.SubnetId subnet-558rhwt2 \
    --InstanceInitInfos.0.Port 3306 \
    --AdminPassword root123 \
    --ClusterName duckduckgogogo \
    --DealMode 0 \
    --OrderSource autotest \
    --PayMode 1 \
    --ProjectId 0 \
    --TimeSpan 1 \
    --TimeUnit m \
    --ResourceTags.0.TagKey autotest \
    --ResourceTags.0.TagValue autotest
```

Output: 
```
{
    "Response": {
        "BigDealIds": [
            "20250515625002861909831"
        ],
        "ClusterIds": [],
        "DealNames": [
            "20250515625002861909861"
        ],
        "RequestId": "cf0a271a-4c08-42e8-96e2-d00ca6167e48",
        "ResourceIds": [],
        "TranId": ""
    }
}
```

