**Example 1: 创建企业信息变更链接**

设置changeType为2，生成企业信息变更链接。

Input: 

```
tccli ess CreateOrganizationInfoChangeUrl --cli-unfold-argument  \
    --Operator.UserId yDwf************************pt7m \
    --ChangeType 2
```

Output: 
```
{
    "Response": {
        "ExpiredTime": 1695780634,
        "RequestId": "f037****-****-****-****-********c036",
        "Url": "https://essurl.cn/003D0UGNSJ "
    }
}
```

**Example 2: 创建超管变更链接**

设置changeType为1，生成超管变更链接。

Input: 

```
tccli ess CreateOrganizationInfoChangeUrl --cli-unfold-argument  \
    --Operator.UserId yDwf************************pt7m \
    --ChangeType 1
```

Output: 
```
{
    "Response": {
        "ExpiredTime": 1695780491,
        "RequestId": "e35e****-****-****-****-********7876",
        "Url": "https://essurl.cn/003D0UGNSJ "
    }
}
```

**Example 3: 创建链接-主代子操作**

主企业代子企业生成企业信息变更链接。

Input: 

```
tccli ess CreateOrganizationInfoChangeUrl --cli-unfold-argument  \
    --Operator.UserId yDwf************************a0uw \
    --Agent.ProxyOrganizationId yDw6************************3Qas \
    --ChangeType 1
```

Output: 
```
{
    "Response": {
        "ExpiredTime": 1695799038,
        "RequestId": "b019****-****-****-****-********ff5f",
        "Url": "https://essurl.cn/003D0UGNSJ "
    }
}
```

**Example 4: 错误示例-变更类型不合法**

设置changeType为3，接口返回错误提示。

Input: 

```
tccli ess CreateOrganizationInfoChangeUrl --cli-unfold-argument  \
    --Operator.UserId yDwf************************pt7m \
    --ChangeType 3
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "InvalidParameter.ParamError",
            "Message": "不支持的变更类型:3,请确认后重新"
        },
        "RequestId": "42df****-****-****-****-********6d37"
    }
}
```

**Example 5: 生成他方企业信息变更链接**



Input: 

```
tccli ess CreateOrganizationInfoChangeUrl --cli-unfold-argument  \
    --Operator.UserId yDwf3UU**********wIpMfa0uw \
    --ChangeType 1 \
    --UnifiedSocialCreditCode 913101*****Q3W
```

Output: 
```
{
    "Response": {
        "ExpiredTime": 1776253917,
        "Url": "https://test.essurl.cn/1c9BUBTlcT",
        "RequestId": "4a332737-9376-438e-b845-274e9a11ad1d"
    }
}
```

