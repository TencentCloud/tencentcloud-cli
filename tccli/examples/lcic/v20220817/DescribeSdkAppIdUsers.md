**Example 1: 获取应用下用户列表**

获取应用下用户列表

Input: 

```
tccli lcic DescribeSdkAppIdUsers --cli-unfold-argument  \
    --SdkAppId 123456
```

Output: 
```
{
    "Response": {
        "Total": 1,
        "Users": [
            {
                "SdkAppId": 1,
                "UserId": "3091",
                "Name": "Name",
                "Avatar": "https://www.dsdjk.png",
                "OriginId": "2CvDgjRNjylAsBZB4iZc0F6koXe"
            }
        ],
        "RequestId": "e574aae1-lp02-4225-a2f8-9032h7199f5f0"
    }
}
```

