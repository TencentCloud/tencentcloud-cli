**Example 1: Sharing an image**

This example shows you how to share an image whose image ID is `img-6pb6lrmy` with the account `1038493875`.

Input: 

```
tccli cvm ModifyImageSharePermission --cli-unfold-argument  \
    --ImageId img-6pb6lrmy\
    --AccountIds 1038493875\
    --Permission SHARE
```

Output: 
```
{
    "Response": {
        "RequestId": "71e69b56-32be-4412-ab45-49eded6a87be"
    }
}
```

