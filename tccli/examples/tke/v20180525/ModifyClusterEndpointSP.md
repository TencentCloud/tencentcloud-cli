**Example 1: Modifying managed cluster public network port’s security policy**



Input: 

```
tccli tke ModifyClusterEndpointSP --cli-unfold-argument  \
    --ClusterId cls-xxxxxxxx \
    --SecurityPolicies 192.168.1.0/24
```

Output: 
```
{
    "Response": {
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

