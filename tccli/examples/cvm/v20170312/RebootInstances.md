**Example 1: Restarting instances**

This example shows you how to restart two instances.

Input: 

```
tccli cvm RebootInstances --cli-unfold-argument  \
    --InstanceIds ins-r8hr2upy ins-5d8a23rs\
    --ForceReboot FALSE
```

Output: 
```
{
    "Response": {
        "RequestId": "6ef60bec-0242-43af-bb20-270359fb54a7"
    }
}
```

