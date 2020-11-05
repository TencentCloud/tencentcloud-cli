**Example 1: Deleting an image**

This example shows you how to delete an image whose image ID is `img-34vaef8fe`. If the image is in use or the image ID does not exist, no operation will be performed and an error code will be returned.

Input: 

```
tccli cvm DeleteImages --cli-unfold-argument  \
    --ImageIds img-34vaef8fe
```

Output: 
```
{
    "Response": {
        "RequestId": "71e69b56-32be-4412-ab45-49eded6a87be"
    }
}
```

