**Example 1: Creating an ES Cluster Instance**

This example shows you how to create an ES cluster instance based on the input parameters

Input: 

```
tccli es CreateInstance --cli-unfold-argument  \
    --EsVersion 6.4.3\
    --ChargeType POSTPAID_BY_HOUR\
    --VpcId vpc-xxxxxx\
    --SubnetId subnet-xxxxxx\
    --Zone ap-guangzhou-3\
    --Password xxxxxx\
    --NodeInfoList.0.Type hotData\
    --NodeInfoList.0.NodeNum 2\
    --NodeInfoList.0.NodeType ES.S1.SMALL2\
    --NodeInfoList.0.DiskType CLOUD_SSD\
    --NodeInfoList.0.DiskSize 100\
    --NodeInfoList.1.Type dedicatedMaster\
    --NodeInfoList.1.NodeNum 3\
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

