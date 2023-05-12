**Example 1: 弹性网卡迁移**

弹性网卡迁移

Input: 

```
tccli vpc MigrateNetworkInterface --cli-unfold-argument  \
    --NetworkInterfaceId eni-afo43z61 \
    --SourceInstanceId ins-r8hr2upy \
    --DestinationInstanceId ins-s2hr8upy
```

Output: 
```
{
    "Response": {
        "RequestId": "f23d1450-ed00-4442-98d4-be409e625e6c"
    }
}
```

