**Example 1: 删除RO组网络**



Input: 

```
tccli postgres DeleteReadOnlyGroupNetworkAccess --cli-unfold-argument  \
    --SubnetId subnet-4s9dejli \
    --VpcId vpc-gaestjaf \
    --Vip 127.0.0.1 \
    --ReadOnlyGroupId pgro-4t9c6g7k
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

