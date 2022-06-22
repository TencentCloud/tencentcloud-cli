**Example 1: 删除实例网络**



Input: 

```
tccli postgres DeleteDBInstanceNetworkAccess --cli-unfold-argument  \
    --SubnetId subnet-4s9dejli \
    --Vip 127.0.01 \
    --VpcId vpc-gaestjaf \
    --DBInstanceId postgres-6bwgamo3
```

Output: 
```
{
    "Response": {
        "RequestId": "6ace8140-6b9e-4e81-a8ad-ef3f92b2aa90",
        "FlowId": 912
    }
}
```

