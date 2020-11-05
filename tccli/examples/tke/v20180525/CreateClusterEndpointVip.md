**Example 1: Creating managed cluster public network access port**



Input: 

```
tccli tke CreateClusterEndpointVip --cli-unfold-argument  \
    --ClusterId cls-xxxxxxxx
```

Output: 
```
{
    "Response": {
        "RequestFlowId": "100000",
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

