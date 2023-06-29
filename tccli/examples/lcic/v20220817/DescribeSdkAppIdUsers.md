**Example 1: 获取应用下用户列表**

获取应用下用户列表

Input: 

```
tccli lcic DescribeSdkAppIdUsers --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Total": 1,
        "Users": [
            {
                "Name": "xx",
                "UserId": "xx",
                "Avatar": "xx",
                "SdkAppId": 1
            }
        ],
        "RequestId": "xx"
    }
}
```

