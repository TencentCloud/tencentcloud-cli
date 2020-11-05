**Example 1: Resetting the password of a Linux/Windows instance**

This example shows you how to reset the password of a Linux/Windows instance, and then use the new password to log in to the instance.

Input: 

```
tccli cvm ResetInstancesPassword --cli-unfold-argument  \
    --InstanceIds ins-r8hr2upy ins-5d8a23rs\
    --Password abc123ABC!@#\
    --ForceStop TRUE
```

Output: 
```
{
    "Response": {
        "RequestId": "6ef60bec-0242-43af-bb20-270359fb54a7"
    }
}
```

