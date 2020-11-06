**Example 1: Resetting the instance model**

This example shows you how to adjust the configuration of an instance that fails to meet your business needs.

Input: 

```
tccli cvm ResetInstancesType --cli-unfold-argument  \
    --InstanceIds ins-r8hr2upy \
    --InstanceType S5.16XLARGE256
```

Output: 
```
{
    "Response": {
        "RequestId": "d39d6c09-44e9-4e80-8661-77b5ff3cbc15"
    }
}
```

