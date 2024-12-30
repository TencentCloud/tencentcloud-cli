**Example 1: 创建企业认证链接**

我们传递企业名称和企业的统一信用代码。同时，为了确保信息的准确性和合规性，我们要求在进行企业认证时，企业名称和统一信用代码必须与我们传递的信息完全一致。

Input: 

```
tccli ess CreateOrganizationAuthUrl --cli-unfold-argument  \
    --Operator.UserId yDwfsUUckpsqt647UE6uSrk1ZWhYH56z \
    --Endpoint SHORT_URL \
    --AuthorizationTypes 1 2 3 \
    --UniformSocialCreditCode 9144030071526726XG \
    --OrganizationName 典子谦示例企业 \
    --UniformSocialCreditCodeSame True \
    --OrganizationNameSame True \
    --Initialization 1
```

Output: 
```
{
    "Response": {
        "AuthUrl": "https://essurl.cn/24VopUGBZyF",
        "ExpiredTime": 1733388643,
        "RequestId": "a34b6e8e-4a3e-444d-8853-b34f90096254"
    }
}
```

**Example 2: 创建企业认证链接-通过授权书上传**

场景：创建企业认证链接， 通过超管授权书上传， 这个场景一般是法人不方便操作的时候使用
授权书的文件生成 可以通过接口[生成企业授权书](https://qian.tencent.com/developers/companyApis/organizations/CreateOrganizationAuthFile) 然后转成 base64 格式。
但是必须得保证超管和创建企业认证是同一个人。

1. AuthorizationTypes 必须且只能传递 1- 授权书认证。
2. PowerOfAttorneys base64 格式的文件流 数组。 单个大小不能超过 8M。



Input: 

```
tccli ess CreateOrganizationAuthUrl --cli-unfold-argument  \
    --Operator.UserId yDwfsUUckpsqt647UE6uSrk1ZWhYH56z \
    --Operator.ClientIp 8.8.8.8 \
    --Endpoint PC \
    --AuthorizationTypes 1 \
    --AdminName 典子谦 \
    --AdminMobile 13200000000 \
    --BusinessLicense base64格式的营业执照文件流 \
    --PowerOfAttorneys base64格式的授权书文件流
```

Output: 
```
{
    "Response": {
        "AuthUrl": "https://test.qian.tencent.cn/console/register-callback?token=yDCYOUUckp7aat8yUxJf7vsvwREPT0Th",
        "ExpiredTime": 1743070967,
        "RequestId": "s1735294966632123121"
    }
}
```

