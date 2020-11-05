**Example 1: Importing an image**

This example shows you how to import an image.

Input: 

```
tccli cvm ImportImage --cli-unfold-argument  \
    --OsType CentOS\
    --OsVersion 6\
    --ImageName sample\
    --ImageDescription sampleimage\
    --ImageUrl http://111-1251233127.cosd.myqcloud.com/Windows%20Server%202008%20R2%20x64a.vmdk\
    --Architecture x86_64
```

Output: 
```
{
    "Response": {
        "RequestId": "71e69b56-32be-4412-ab45-49eded6a87be"
    }
}
```

