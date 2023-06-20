**Example 1: 创建RO组网络**

创建RO组网络

Input: 

```
tccli postgres CreateReadOnlyGroupNetworkAccess --cli-unfold-argument  \
    --SubnetId subnet-4s9dejli \
    --VpcId vpc-gaestjaf \
    --ReadOnlyGroupId pgro-4t9c6g7k \
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

