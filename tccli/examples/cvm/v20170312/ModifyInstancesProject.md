**Example 1: Modifying the projects of two instances**

This example shows you how to change the projects of two instances to a specified one.

Input: 

```
tccli cvm ModifyInstancesProject --cli-unfold-argument  \
    --InstanceIds ins-r8hr2upy ins-5d8a23rs \
    --ProjectId 1045
```

Output: 
```
{
    "Response": {
        "RequestId": "6ef60bec-0242-43af-bb20-270359fb54a7"
    }
}
```

