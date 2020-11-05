**Example 1: Modifying an ENI**



Input: 

```
tccli vpc ModifyNetworkInterfaceAttribute --cli-unfold-argument  \
    --Version 2017-03-12\
    --NetworkInterfaceId eni-afo43z61\
    --NetworkInterfaceName NewName
```

Output: 
```
{
    "Response": {
        "RequestId": "f23d1450-ed00-4442-98d4-be409e625e6c"
    }
}
```

