**Example 1: 删除RO组网络**



Input: 

```
tccli postgres DeleteReadOnlyGroupNetworkAccess --cli-unfold-argument  \
    --ReadOnlyGroupId pgro-4t9c6g7k \
    --VpcId vpc-gaestjaf \
    --SubnetId subnet-4s9dejli \
    --Vip 127.0.0.1
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

