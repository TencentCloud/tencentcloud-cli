**Example 1: 创建管理端登录链接示例**

创建管理端登录链接示例

Input: 

```
tccli ccc CreateAdminURL --cli-unfold-argument  \
    --SdkAppId 1400000000 \
    --SeatUserId foo@tencent.com
```

Output: 
```
{
    "Response": {
        "RequestId": "48edd236-7ef1-45af-9e12-fc376ba355bf",
        "URL": "https://tccc.qcloud.com/saas-manage/#/1400000000/home?token=6bb56a09-2787-40bc-80c5-dc6dab783eff"
    }
}
```

