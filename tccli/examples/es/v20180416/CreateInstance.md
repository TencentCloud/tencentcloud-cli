**Example 1: 创建ES集群实例**

根据输入参数创建ES集群实例

Input: 

```
tccli es CreateInstance --cli-unfold-argument  \
    --EsVersion 6.4.3 \
    --VpcId vpc-xxxxxx \
    --NodeInfoList.0.NodeType ES.S1.SMALL2 \
    --NodeInfoList.0.NodeNum 3 \
    --NodeInfoList.0.Type dedicatedMaster \
    --NodeInfoList.1.DiskSize 100 \
    --NodeInfoList.1.NodeType ES.S1.SMALL2 \
    --NodeInfoList.1.NodeNum 2 \
    --NodeInfoList.1.Type hotData \
    --NodeInfoList.1.DiskType CLOUD_SSD \
    --Zone ap-guangzhou-3 \
    --ChargeType POSTPAID_BY_HOUR \
    --SubnetId subnet-xxxxxx \
    --Password xxxxxx \
    --InstanceName es_test
```

Output: 
```
{
    "Response": {
        "InstanceId": "ab",
        "RequestId": "ab",
        "DealName": "ab"
    }
}
```

