**Example 1: 批量注册三家企业,成功创建任务**



Input: 

```
tccli ess CreateBatchOrganizationRegistrationTasks --cli-unfold-argument  \
    --Operator.OpenId us-768d38720c10405f994539097f030a27 \
    --Operator.UserId 19561039c99fe825a934a132520fde6a \
    --Operator.Channel YUFU \
    --Operator.ClientIp 8.8.8.8 \
    --RegistrationOrganizations.0.OrganizationName 测试认证企业一 \
    --RegistrationOrganizations.0.UniformSocialCreditCode 9XXXXXXXXXXXXXXXX1 \
    --RegistrationOrganizations.0.LegalName 鹅鹅子 \
    --RegistrationOrganizations.0.Address 深圳市南山区1000号腾讯大厦 \
    --RegistrationOrganizations.0.AdminName 鹅鹅子 \
    --RegistrationOrganizations.0.AdminMobile 187XXXXXXX0 \
    --RegistrationOrganizations.0.AuthorizationTypes 2 \
    --RegistrationOrganizations.1.OrganizationName 测试认证企业二 \
    --RegistrationOrganizations.1.UniformSocialCreditCode 9XXXXXXXXXXXXXXXX2 \
    --RegistrationOrganizations.1.LegalName 鹅鹅子 \
    --RegistrationOrganizations.1.Address 深圳市南山区1000号腾讯大厦 \
    --RegistrationOrganizations.1.AdminName 鹅鹅子 \
    --RegistrationOrganizations.1.AdminMobile 187XXXXXXX0 \
    --RegistrationOrganizations.1.AuthorizationTypes 1 \
    --RegistrationOrganizations.2.OrganizationName 测试认证企业三 \
    --RegistrationOrganizations.2.UniformSocialCreditCode 9XXXXXXXXXXXXXXXX3 \
    --RegistrationOrganizations.2.LegalName 鹅鹅子 \
    --RegistrationOrganizations.2.Address 深圳市南山区1000号腾讯大厦 \
    --RegistrationOrganizations.2.AdminName 鹅鹅子 \
    --RegistrationOrganizations.2.AdminMobile 187XXXXXXX0 \
    --RegistrationOrganizations.2.AuthorizationTypes 2
```

Output: 
```
{
    "Response": {
        "TaskId": "abc",
        "ErrorMessages": [
            ""
        ],
        "RequestId": "f38013e59d00"
    }
}
```

**Example 2: 批量注册三家企业,地址不符合格式,返回错误**

测试认证企业三的地址没有按照省市区的格式传递

Input: 

```
tccli ess CreateBatchOrganizationRegistrationTasks --cli-unfold-argument  \
    --Operator.OpenId us-768d38720c10405f994539097f030a27 \
    --Operator.UserId 19561039c99fe825a934a132520fde6a \
    --Operator.Channel YUFU \
    --Operator.ClientIp 8.8.8.8 \
    --RegistrationOrganizations.0.OrganizationName 测试认证企业一 \
    --RegistrationOrganizations.0.UniformSocialCreditCode 9XXXXXXXXXXXXXXXX1 \
    --RegistrationOrganizations.0.LegalName 鹅鹅子 \
    --RegistrationOrganizations.0.Address 深圳市南山区1000号腾讯大厦 \
    --RegistrationOrganizations.0.AdminName 鹅鹅子 \
    --RegistrationOrganizations.0.AdminMobile 187XXXXXXX0 \
    --RegistrationOrganizations.0.AuthorizationTypes 2 \
    --RegistrationOrganizations.1.OrganizationName 测试认证企业二 \
    --RegistrationOrganizations.1.UniformSocialCreditCode 9XXXXXXXXXXXXXXXX2 \
    --RegistrationOrganizations.1.LegalName 鹅鹅子 \
    --RegistrationOrganizations.1.Address 深圳市南山区1000号腾讯大厦 \
    --RegistrationOrganizations.1.AdminName 鹅鹅子 \
    --RegistrationOrganizations.1.AdminMobile 187XXXXXXX0 \
    --RegistrationOrganizations.1.AuthorizationTypes 1 \
    --RegistrationOrganizations.2.OrganizationName 测试认证企业三 \
    --RegistrationOrganizations.2.UniformSocialCreditCode 9XXXXXXXXXXXXXXXX3 \
    --RegistrationOrganizations.2.LegalName 鹅鹅子 \
    --RegistrationOrganizations.2.Address 测试地址 \
    --RegistrationOrganizations.2.AdminName 鹅鹅子 \
    --RegistrationOrganizations.2.AdminMobile 187XXXXXXX0 \
    --RegistrationOrganizations.2.AuthorizationTypes 2
```

Output: 
```
{
    "Response": {
        "ErrorMessages": [
            "",
            "第【2】条注册信息参数错误，地址参数不正确,请确认后再试",
            ""
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
tccli ess CreateBatchOrganizationRegistrationTasks --cli-unfold-argument  \
    --Operator.OpenId us-768d38720c10405f994539097f030a27 \
    --Operator.UserId 19561039c99fe825a934a132520fde6a \
    --Operator.Channel YUFU \
    --Operator.ClientIp 8.8.8.8 \
    --RegistrationOrganizations.0.OrganizationName 测试认证企业一 \
    --RegistrationOrganizations.0.UniformSocialCreditCode 9XXXXXXXXXXXXXXXX1 \
    --RegistrationOrganizations.0.LegalName 鹅鹅子 \
    --RegistrationOrganizations.0.Address 深圳市南山区1000号腾讯大厦 \
    --RegistrationOrganizations.0.AdminName 鹅鹅子 \
    --RegistrationOrganizations.0.AdminMobile 187XXXXXXX0 \
    --RegistrationOrganizations.0.AuthorizationTypes 2 \
    --RegistrationOrganizations.1.OrganizationName 测试认证企业二 \
    --RegistrationOrganizations.1.UniformSocialCreditCode 9XXXXXXXXXXXXXXXX2 \
    --RegistrationOrganizations.1.LegalName 鹅鹅子 \
    --RegistrationOrganizations.1.Address 深圳市南山区1000号腾讯大厦 \
    --RegistrationOrganizations.1.AdminName 鹅鹅子 \
    --RegistrationOrganizations.1.AdminMobile 187XXXXXXX0 \
    --RegistrationOrganizations.1.AuthorizationTypes 1 \
    --RegistrationOrganizations.2.OrganizationName 测试认证企业一 \
    --RegistrationOrganizations.2.UniformSocialCreditCode 9XXXXXXXXXXXXXXXX3 \
    --RegistrationOrganizations.2.LegalName 鹅鹅子 \
    --RegistrationOrganizations.2.Address 深圳市南山区1000号腾讯大厦 \
    --RegistrationOrganizations.2.AdminName 鹅鹅子 \
    --RegistrationOrganizations.2.AdminMobile 187XXXXXXX0 \
    --RegistrationOrganizations.2.AuthorizationTypes 2
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

