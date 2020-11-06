**Example 1: Modifying the public network bandwidth cap of an instance**

This example shows you how to modify the public network bandwidth cap of an instance.

Input: 

```
tccli cvm ResetInstancesInternetMaxBandwidth --cli-unfold-argument  \
    --InstanceIds ins-r8hr2upy \
    --InternetAccessible.InternetMaxBandwidthOut 10 \
    --StartTime 2017-03-15 \
    --EndTime 2017-03-16
```

Output: 
```
{
    "Response": {
        "RequestId": "d39d6c09-44e9-4e80-8661-77b5ff3cbc15"
    }
}
```

