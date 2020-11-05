**Example 1: Binding an ENI to a CVM**



Input: 

```
tccli vpc AttachNetworkInterface --cli-unfold-argument  \
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

