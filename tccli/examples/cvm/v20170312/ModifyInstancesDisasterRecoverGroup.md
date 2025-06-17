**Example 1: 调整实例所在置放群组**

调整实例所在置放群组

Input: 

```
tccli cvm ModifyInstancesDisasterRecoverGroup --cli-unfold-argument  \
    --InstanceIds ins-r8hr2upy \
    --DisasterRecoverGroupId ps-a66w6rlb
```

Output: 
```
{
    "Response": {
        "RequestId": "d39d6c09-44e9-4e80-8661-77b5ff3cbc15"
    }
}
```

