**Example 1: 创建专业集群**

创建专业集群 -- 仅通过api调用

Input: 

```
tccli tdmq CreateProCluster --cli-unfold-argument  \
    --ZoneIds 200002 200003 200004 \
    --ProductName devTest \
    --StorageSize 0 \
    --AutoRenewFlag 0 \
    --TimeSpan 0 \
    --Vpc.VpcId vpc-8jiausye \
    --Vpc.SubnetId subnet-1iuyhzke \
    --Tags.0.TagKey devTag \
    --Tags.0.TagValue dev \
    --ClusterName devTest \
    --AutoVoucher 0
```

Output: 
```
{
    "Response": {
        "DealName": "202403206137826783502561 ",
        "BigDealId": "202403206137826783502561 ",
        "ClusterId": "pulsar-x4r939zkwmm2",
        "ClusterName": "devTest",
        "RequestId": "0799dd77-707b-40d7-a4b5-4140b11f6c97"
    }
}
```

