**Example 1: 开启注册节点池支持**



Input: 

```
tccli tke EnableExternalNodeSupport --cli-unfold-argument  \
    --ClusterId cls-edk3h1cs \
    --ClusterExternalConfig.NetworkType HostNetwork \
    --ClusterExternalConfig.SubnetId subnet-1ed3gqns \
    --ClusterExternalConfig.Enabled True
```

Output: 
```
{
    "Response": {
        "RequestId": "ea4ba3bb-b020-42a3-932e-0a33a88182be"
    }
}
```

