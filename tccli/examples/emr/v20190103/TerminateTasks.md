**Example 1: Terminating a node**

This example shows you how to terminate a task node.

Input: 

```
tccli emr TerminateTasks --cli-unfold-argument  \
    --InstanceId emr-4slr7ad7 \
    --ResourceIds emr-vm-xxx33tg
```

Output: 
```
{
    "Response": {
        "RequestId": "4d701c1e-8507-47e1-8c69-a8f06a236f24"
    }
}
```

