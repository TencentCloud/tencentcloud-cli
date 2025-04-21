**Example 1: 获取企业微信第三方应用安装授权链接**

获取企业微信第三方应用安装授权链接

Input: 

```
tccli ioa DescribeWeComAppInstallInfo --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Data": {
            "Url": "https://tencent.com/xxxx",
            "ExpiresIn": 3600
        },
        "RequestId": "xx"
    }
}
```

