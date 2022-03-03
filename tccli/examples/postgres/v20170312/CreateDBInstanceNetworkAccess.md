**Example 1: 添加实例网络**



Input: 

```
tccli postgres CreateDBInstanceNetworkAccess --cli-unfold-argument  \
    --DBInstanceId postgres-6bwgamo3 \
    --VpcId vpc-gaestjaf \
    --SubnetId subnet-4s9dejli \
    --IsAssignVip false
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

