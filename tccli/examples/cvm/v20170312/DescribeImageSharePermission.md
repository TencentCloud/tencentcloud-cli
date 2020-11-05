**Example 1: Querying sharing information of a specified image**

This example shows you how to query the sharing information of an image whose image ID is img-6pb6lrmy.

Input: 

```
tccli cvm DescribeImageSharePermission --cli-unfold-argument  \
    --ImageId img-6pb6lrmy
```

Output: 
```
{
    "Response": {
        "SharePermissionSet": [
            {
                "CreatedTime": "2018-06-10T11:02:50Z",
                "AccountId": "101104350000"
            },
            {
                "CreatedTime": "2018-06-13T15:03:25Z",
                "AccountId": "101104350001"
            }
        ],
        "RequestId": "71e69b56-32be-4412-ab45-49eded6a87be"
    }
}
```

