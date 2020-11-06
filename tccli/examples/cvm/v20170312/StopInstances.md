**Example 1: Shutting down instances**

This example shows you how to shut down two instances.

Input: 

```
tccli cvm StopInstances --cli-unfold-argument  \
    --InstanceIds ins-r8hr2upy ins-5d8a23rs \
    --ForceStop FALSE
```

Output: 
```
{
    "Response": {
        "RequestId": "6ef60bec-0242-43af-bb20-270359fb54a7"
    }
}
```

