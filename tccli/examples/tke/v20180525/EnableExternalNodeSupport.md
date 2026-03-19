**Example 1: 开启第三方节点池支持**



Input: 

```
tccli tke EnableExternalNodeSupport --cli-unfold-argument  \
    --ClusterId cls-lm91rql0 \
    --ClusterExternalConfig.ClusterCIDR 172.22.0.0/16 \
    --ClusterExternalConfig.NetworkType CiliumVXLan \
    --ClusterExternalConfig.SubnetId subnet-drsvvxxx
```

Output: 
```
{
    "Response": {
        "RequestId": "4c6c63c7-b23e-4896-bf3b-6bc44dxxxxxx"
    }
}
```

