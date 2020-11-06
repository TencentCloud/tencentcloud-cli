**Example 1: Modifying instance names**

This example shows you how to modify the names of two instances.

Input: 

```
tccli cvm ModifyInstancesAttribute --cli-unfold-argument  \
    --InstanceIds ins-r8hr2upy ins-5d8a23rs \
    --InstanceName Mysql_Server
```

Output: 
```
{
    "Response": {
        "RequestId": "6ef60bec-0242-43af-bb20-270359fb54a7"
    }
}
```

