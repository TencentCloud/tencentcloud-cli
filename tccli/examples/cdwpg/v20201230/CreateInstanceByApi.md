**Example 1: 创建集群**

创建集群

Input: 

```
tccli cdwpg CreateInstanceByApi --cli-unfold-argument  \
    --InstanceName abc \
    --Zone abc \
    --UserVPCId abc \
    --UserSubnetId abc \
    --ChargeProperties.PayMode 0 \
    --ChargeProperties.RenewFlag 0 \
    --ChargeProperties.TimeSpan 0 \
    --ChargeProperties.TimeUnit abc \
    --ChargeProperties.ChargeType abc \
    --AdminPassword abc \
    --Tags.TagKey abc \
    --Tags.TagValue abc \
    --Resources.0.SpecName abc \
    --Resources.0.Count 0 \
    --Resources.0.DiskSpec.DiskType abc \
    --Resources.0.DiskSpec.DiskSize 0 \
    --Resources.0.DiskSpec.DiskCount 0 \
    --Resources.0.Type abc
```

Output: 
```
{
    "Response": {
        "FlowId": "abc",
        "InstanceId": "abc",
        "ErrorMsg": "abc",
        "RequestId": "abc"
    }
}
```

