**Example 1: Unbinding an ENI from a CVM**



Input: 

```
tccli vpc DetachNetworkInterface --cli-unfold-argument  \
    --Version 2017-03-12\
    --NetworkInterfaceId eni-afo43z61\
    --InstanceId ins-ins-r8hr2upy
```

Output: 
```
{
    "Response": {
        "RequestId": "f23d1450-ed00-4442-98d4-be409e625e6c"
    }
}
```

