**Example 1: 创建专业集群**



Input: 

```
tccli tdmq CreateProCluster --cli-unfold-argument  \
    --ZoneIds abc \
    --ProductName abc \
    --StorageSize 0 \
    --AutoRenewFlag 0 \
    --TimeSpan 0 \
    --Vpcs.VpcId abc \
    --Vpcs.SubnetId abc \
    --Tags.0.TagKey abc \
    --Tags.0.TagValue abc \
    --ClusterName abc \
    --AutoVoucher 0
```

Output: 
```
{
    "Response": {
        "DealName": "abc",
        "BigDealId": "abc",
        "ClusterId": "abc",
        "ClusterName": "abc",
        "RequestId": "abc"
    }
}
```

