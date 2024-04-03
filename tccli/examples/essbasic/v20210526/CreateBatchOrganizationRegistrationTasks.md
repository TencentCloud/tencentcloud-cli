**Example 1: 批量生成企业注册链接成功**

用户同时创建3个企业， 创建链接成功

Input: 

```
tccli essbasic CreateBatchOrganizationRegistrationTasks --cli-unfold-argument  \
    --Agent.ProxyOperator.OpenId ceshi \
    --Agent.ProxyOrganizationOpenId ceshi_org \
    --Agent.AppId 60e16350b0361c888ecb30477d2c16e9 \
    --RegistrationOrganizations.0.OrganizationName 测试认证企业一 \
    --RegistrationOrganizations.0.UniformSocialCreditCode 9XXXXXXXXXXXXXXXX1 \
    --RegistrationOrganizations.0.LegalName 鹅鹅子 \
    --RegistrationOrganizations.0.Address 深圳市南山区1000号腾讯大厦 \
    --RegistrationOrganizations.0.AdminName 鹅鹅子 \
    --RegistrationOrganizations.0.AdminMobile 187XXXXXXX0 \
    --RegistrationOrganizations.0.AuthorizationTypes 1 \
    --RegistrationOrganizations.0.OrganizationOpenId 1 \
    --RegistrationOrganizations.0.OpenId 1 \
    --RegistrationOrganizations.1.OrganizationName 测试认证企业二 \
    --RegistrationOrganizations.1.UniformSocialCreditCode 9XXXXXXXXXXXXXXXX2 \
    --RegistrationOrganizations.1.LegalName 鹅鹅子 \
    --RegistrationOrganizations.1.Address 深圳市南山区1000号腾讯大厦 \
    --RegistrationOrganizations.1.AdminName 鹅鹅子 \
    --RegistrationOrganizations.1.AdminMobile 187XXXXXXX0 \
    --RegistrationOrganizations.1.AuthorizationTypes 1 \
    --RegistrationOrganizations.1.OrganizationOpenId 2 \
    --RegistrationOrganizations.1.OpenId 2 \
    --RegistrationOrganizations.2.OrganizationName 测试认证企业三 \
    --RegistrationOrganizations.2.UniformSocialCreditCode 9XXXXXXXXXXXXXXXX3 \
    --RegistrationOrganizations.2.LegalName 鹅鹅子 \
    --RegistrationOrganizations.2.Address 深圳市南山区1000号腾讯大厦 \
    --RegistrationOrganizations.2.AdminName 鹅鹅子 \
    --RegistrationOrganizations.2.AdminMobile 187XXXXXXX0 \
    --RegistrationOrganizations.2.AuthorizationTypes 2 \
    --RegistrationOrganizations.2.OrganizationOpenId 3 \
    --RegistrationOrganizations.2.OpenId 3
```

Output: 
```
{
    "Response": {
        "ErrorMessages": [],
        "RequestId": "f38013e59d00",
        "TaskId": "yDRBJUUgygqwl721UuO4zjECcJHV2RAi"
    }
}
```

**Example 2: 批量注册三家企业,地址不符合格式,返回错误**

测试认证企业三的地址没有按照省市区的格式传递

Input: 

```
tccli essbasic CreateBatchOrganizationRegistrationTasks --cli-unfold-argument  \
    --Agent.ProxyOperator.OpenId ceshi \
    --Agent.ProxyOrganizationOpenId ceshi_org \
    --Agent.AppId 60e16350b0361c888ecb30477d2c16e9 \
    --RegistrationOrganizations.0.OrganizationName 测试认证企业一 \
    --RegistrationOrganizations.0.UniformSocialCreditCode 9XXXXXXXXXXXXXXXX1 \
    --RegistrationOrganizations.0.LegalName 鹅鹅子 \
    --RegistrationOrganizations.0.Address 深圳市南山区1000号腾讯大厦 \
    --RegistrationOrganizations.0.AdminName 鹅鹅子 \
    --RegistrationOrganizations.0.AdminMobile 187XXXXXXX0 \
    --RegistrationOrganizations.0.AuthorizationTypes 1 \
    --RegistrationOrganizations.0.OrganizationOpenId 1 \
    --RegistrationOrganizations.0.OpenId 1 \
    --RegistrationOrganizations.1.OrganizationName 测试认证企业二 \
    --RegistrationOrganizations.1.UniformSocialCreditCode 9XXXXXXXXXXXXXXXX2 \
    --RegistrationOrganizations.1.LegalName 鹅鹅子 \
    --RegistrationOrganizations.1.Address 深圳市南山区1000号腾讯大厦 \
    --RegistrationOrganizations.1.AdminName 鹅鹅子 \
    --RegistrationOrganizations.1.AdminMobile 187XXXXXXX0 \
    --RegistrationOrganizations.1.AuthorizationTypes 1 \
    --RegistrationOrganizations.1.OrganizationOpenId 2 \
    --RegistrationOrganizations.1.OpenId 2 \
    --RegistrationOrganizations.2.OrganizationName 测试认证企业三 \
    --RegistrationOrganizations.2.UniformSocialCreditCode 9XXXXXXXXXXXXXXXX3 \
    --RegistrationOrganizations.2.LegalName 鹅鹅子 \
    --RegistrationOrganizations.2.Address 1000号腾讯大厦 \
    --RegistrationOrganizations.2.AdminName 鹅鹅子 \
    --RegistrationOrganizations.2.AdminMobile 187XXXXXXX0 \
    --RegistrationOrganizations.2.AuthorizationTypes 1 \
    --RegistrationOrganizations.2.OrganizationOpenId 3 \
    --RegistrationOrganizations.2.OpenId 3
```

Output: 
```
{
    "Response": {
        "ErrorMessages": [
            "",
            "",
            "第【3】条注册信息参数错误，地址参数不正确,请确认后再试"
        ],
        "RequestId": "5cea4b4778bf",
        "TaskId": ""
    }
}
```

**Example 3: 批量注册三家企业,企业名称重复,无法创建,返回错误提示**

第一家企业和第三家企业名字重复, 无法注册

Input: 

```
tccli essbasic CreateBatchOrganizationRegistrationTasks --cli-unfold-argument  \
    --Agent.ProxyOperator.OpenId ceshi \
    --Agent.ProxyOrganizationOpenId ceshi_org \
    --Agent.AppId 60e16350b0361c888ecb30477d2c16e9 \
    --RegistrationOrganizations.0.OrganizationName 测试认证企业一 \
    --RegistrationOrganizations.0.UniformSocialCreditCode 9XXXXXXXXXXXXXXXX1 \
    --RegistrationOrganizations.0.LegalName 鹅鹅子 \
    --RegistrationOrganizations.0.Address 深圳市南山区1000号腾讯大厦 \
    --RegistrationOrganizations.0.AdminName 鹅鹅子 \
    --RegistrationOrganizations.0.AdminMobile 187XXXXXXX0 \
    --RegistrationOrganizations.0.AuthorizationTypes 1 \
    --RegistrationOrganizations.0.OrganizationOpenId 1 \
    --RegistrationOrganizations.0.OpenId 1 \
    --RegistrationOrganizations.1.OrganizationName 测试认证企业二 \
    --RegistrationOrganizations.1.UniformSocialCreditCode 9XXXXXXXXXXXXXXXX2 \
    --RegistrationOrganizations.1.LegalName 鹅鹅子 \
    --RegistrationOrganizations.1.Address 深圳市南山区1000号腾讯大厦 \
    --RegistrationOrganizations.1.AdminName 鹅鹅子 \
    --RegistrationOrganizations.1.AdminMobile 187XXXXXXX0 \
    --RegistrationOrganizations.1.AuthorizationTypes 1 \
    --RegistrationOrganizations.1.OrganizationOpenId 2 \
    --RegistrationOrganizations.1.OpenId 2 \
    --RegistrationOrganizations.2.OrganizationName 测试认证企业一 \
    --RegistrationOrganizations.2.UniformSocialCreditCode 9XXXXXXXXXXXXXXXX3 \
    --RegistrationOrganizations.2.LegalName 鹅鹅子 \
    --RegistrationOrganizations.2.Address 深圳市南山区1000号腾讯大厦 \
    --RegistrationOrganizations.2.AdminName 鹅鹅子 \
    --RegistrationOrganizations.2.AdminMobile 187XXXXXXX0 \
    --RegistrationOrganizations.2.AuthorizationTypes 1 \
    --RegistrationOrganizations.2.OrganizationOpenId 3 \
    --RegistrationOrganizations.2.OpenId 3
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "InvalidParameterValue",
            "Message": "企业名称[测试认证企业一]重复"
        },
        "RequestId": "4f7b42be805f"
    }
}
```

