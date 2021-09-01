**Example 1: 创建ES集群实例**

根据输入参数创建ES集群实例

Input: 

```
tccli es CreateInstance --cli-unfold-argument  \
    --InstanceName es_test \
    --EsVersion 6.4.3 \
    --ChargeType POSTPAID_BY_HOUR \
    --VpcId vpc-xxxxxx \
    --SubnetId subnet-xxxxxx \
    --Zone ap-guangzhou-3 \
    --Password xxxxxx \
    --NodeInfoList.0.Type hotData \
    --NodeInfoList.0.NodeNum 2 \
    --NodeInfoList.0.NodeType ES.S1.SMALL2 \
    --NodeInfoList.0.DiskType CLOUD_SSD \
    --NodeInfoList.0.DiskSize 100 \
    --NodeInfoList.1.Type dedicatedMaster \
    --NodeInfoList.1.NodeNum 3 \
    --NodeInfoList.1.NodeType ES.S1.SMALL2
```

Output: 
```
{
    "Response": {
        "InstanceId": "es-xxxxxx",
        "RequestId": "d7b76d5e-ad7d-4abd-b3b2-43b96dxxxxxx"
    }
}
```

