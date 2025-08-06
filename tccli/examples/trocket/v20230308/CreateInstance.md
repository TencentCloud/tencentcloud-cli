**Example 1: 正常响应**

成功创建一个 TPS 2000 的 RocketMQ 5.x 集群。

Input: 

```
tccli trocket CreateInstance --cli-unfold-argument  \
    --InstanceType BASIC \
    --Name test_instance \
    --SkuCode basic_2k \
    --VpcList.0.VpcId vpc-xxxx \
    --VpcList.0.SubnetId subnet-xxxx
```

Output: 
```
{
    "Error": null,
    "RequestId": null,
    "Response": {
        "InstanceId": "rmq-72mo3a9or",
        "RequestId": "32759095-0372-4ec0-ae3a-e5a2759fd0ff"
    }
}
```

