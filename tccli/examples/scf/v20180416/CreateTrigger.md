**Example 1: Creating a trigger**

This example shows you how to use this function to create a trigger.

Input: 

```
tccli scf CreateTrigger --cli-unfold-argument  \
    --FunctionName <FunctionName> \
    --TriggerName <TriggerName> \
    --Type timer \
    --TriggerDesc */2****
```

Output: 
```
{
    "Response": {
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

