**Example 1: Modifying image name**

This example shows you how to change the name of an image whose image ID is `img-6pb6lrmy` to "sample".

Input: 

```
tccli cvm ModifyImageAttribute --cli-unfold-argument  \
    --ImageId img-6pb6lrmy \
    --ImageName sample
```

Output: 
```
{
    "Response": {
        "RequestId": "71e69b56-32be-4412-ab45-49eded6a87be"
    }
}
```

