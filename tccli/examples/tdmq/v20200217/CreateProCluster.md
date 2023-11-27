**Example 1: 创建专业集群**

创建专业集群 -- 仅通过api调用

Input: 

```
tccli tdmq CreateProCluster --cli-unfold-argument  \
    --ZoneIds 200002 200003 200004 \
    --ProductName abc \
    --StorageSize 0 \
    --AutoRenewFlag 0 \
    --TimeSpan 0 \
    --Vpc.VpcId abc \
    --Vpc.SubnetId abc \
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

