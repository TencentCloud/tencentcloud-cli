**Example 1: Creating an image**

This example shows you how to create an image from the instance “ins-6pb6lrmy”. If the instance is running, perform a soft shutdown. If the soft shutdown fails, the task will end (default semantics).

Input: 

```
tccli cvm CreateImage --cli-unfold-argument  \
    --InstanceId ins-6pb6lrmy \
    --ImageName "name"
```

Output: 
```
{
    "Response": {
        "ImageId": "img-0yc6rie8",
        "RequestId": "71e69b56-32be-4412-ab45-49eded6a87be"
    }
}
```

