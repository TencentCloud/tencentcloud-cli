**Example 1: 创建专业集群**

创建专业集群 -- 仅通过api调用

Input: 

```
tccli tdmq CreateProCluster --cli-unfold-argument  \
    --ZoneIds 200002 200003 200004 \
    --ProductName PULSAR.P1.MINI2 \
    --StorageSize 400 \
    --AutoRenewFlag 0 \
    --TimeSpan 1 \
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

**Example 2: 创建标准版集群**

创建标准版集群，使用 3.0 版本

Input: 

```
tccli tdmq CreateProCluster --cli-unfold-argument  \
    --ZoneIds 200002 200003 \
    --ProductName PULSAR.S2.MINI1 \
    --AutoRenewFlag 0 \
    --TimeSpan 1 \
    --Vpc.VpcId vpc-8jiausye \
    --Vpc.SubnetId subnet-1iuyhzke \
    --Tags.0.TagKey devTag \
    --Tags.0.TagValue dev \
    --InstanceVersion 3.0.0 \
    --ClusterName devTest \
    --AutoVoucher 0
```

Output: 
```
{
    "Response": {
        "BigDealId": "20260622622023050338201",
        "ClusterId": "pulsar-jmajx4jqgbzz",
        "ClusterName": "devTest",
        "DealName": "20260622622023050338211",
        "RequestId": "59458479-9217-4202-a210-1aa4d249dbc6"
    }
}
```

