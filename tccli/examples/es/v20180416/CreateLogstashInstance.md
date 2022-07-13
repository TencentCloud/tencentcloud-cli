**Example 1: 创建Logstash实例**

根据输入参数创建Logstash实例

Input: 

```
tccli es CreateLogstashInstance --cli-unfold-argument  \
    --InstanceName logstash_test \
    --LogstashVersion 6.8.13 \
    --ChargeType POSTPAID_BY_HOUR \
    --VpcId vpc-xxxxxx \
    --SubnetId subnet-xxxxxx \
    --Zone ap-guangzhou-3 \
    --DiskType CLOUD_SSD \
    --DiskSize 100 \
    --NodeNum 3 \
    --NodeType LOGSTASH.S1.SMALL2
```

Output: 
```
{
    "Response": {
        "InstanceId": "ls-xxxxxx",
        "RequestId": "d7b76d5e-ad7d-4abd-b3b2-43b96dxxxxxx"
    }
}
```

