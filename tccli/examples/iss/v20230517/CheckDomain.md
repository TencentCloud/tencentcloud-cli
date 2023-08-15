**Example 1: 成功**

 

Input: 

```
tccli iss CheckDomain --cli-unfold-argument  \
    --PlayDomain testdomain.cn \
    --InternalDomain *******************************.play-ivc.ap-shanghai.tencentivc.cn
```

Output: 
```
{
    "Response": {
        "Data": true,
        "RequestId": "e565e8fe-127c-442c-8912-55b0e11d8ab4"
    }
}
```

**Example 2: 错误**

域名存在

Input: 

```
tccli iss CheckDomain --cli-unfold-argument  \
    --PlayDomain testdomain.cn \
    --InternalDomain ****************************.play-ivc.ap-shanghai.tencentivc.cn
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "InvalidParameterValue.DomainRepeat",
            "Message": "该域名已存在"
        },
        "RequestId": "9e9b6808-0941-41e9-95eb-5a9a827ca4de"
    }
}
```

