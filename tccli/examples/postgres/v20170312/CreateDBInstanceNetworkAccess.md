**Example 1: 创建实例网络**

创建实例网络

Input: 

```
tccli postgres CreateDBInstanceNetworkAccess --cli-unfold-argument  \
    --SubnetId subnet-4s9dejli \
    --VpcId vpc-gaestjaf \
    --DBInstanceId postgres-6bwgamo3 \
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

