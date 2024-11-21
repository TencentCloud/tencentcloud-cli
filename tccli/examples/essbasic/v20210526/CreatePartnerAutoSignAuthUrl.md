**Example 1: 授权给渠道平台应用**



Input: 

```
tccli essbasic CreatePartnerAutoSignAuthUrl --cli-unfold-argument  \
    --Agent.AppId yDwhxUUckp3gl8j5UuFX33LSNozpRsbi \
    --Agent.ProxyOrganizationOpenId org_dianziqian \
    --Agent.ProxyOperator.OpenId n9527 \
    --PlatformAppAuthorization True
```

Output: 
```
{
    "Response": {
        "ExpireTime": 1702982931,
        "MiniAppPath": "/pages/guide/index?shortKey=002XCUHfPi ",
        "RequestId": "49500cb4-ca5e-4da0-93fb-e15f3a710ed7 ",
        "Url": "https://essurl.cn/003hGUFil8 "
    }
}
```

**Example 2: 我方授权他方**

授权给张三示例企业能发完我方的自动签署的合同

Input: 

```
tccli essbasic CreatePartnerAutoSignAuthUrl --cli-unfold-argument  \
    --Agent.AppId yDwhxUUckp3gl8j5UuFX33LSNozpRsbi \
    --Agent.ProxyOrganizationOpenId org_dianziqian \
    --Agent.ProxyOperator.OpenId n9527 \
    --AuthorizedOrganizationName 张三示例企业 \
    --SealTypes OFFICIAL
```

Output: 
```
{
    "Response": {
        "ExpireTime": 1702982931,
        "MiniAppPath": "/pages/guide/index?shortKey=002XCUHfPi ",
        "RequestId": "49500cb4-ca5e-4da0-93fb-e15f3a710ed7 ",
        "Url": "https://essurl.cn/003hGUFil8 "
    }
}
```

**Example 3: 他方授权我方**

让王五示例企业授权给我方能发起他们的自动签署合同

Input: 

```
tccli essbasic CreatePartnerAutoSignAuthUrl --cli-unfold-argument  \
    --Agent.AppId yDwhxUUckp3gl8j5UuFX33LSNozpRsbi \
    --Agent.ProxyOrganizationOpenId org_dianziqian \
    --Agent.ProxyOperator.OpenId n9527 \
    --AuthorizedOrganizationName 王五示例企业 \
    --AuthToMe True \
    --SealTypes OFFICIAL
```

Output: 
```
{
    "Response": {
        "ExpireTime": 1702982931,
        "MiniAppPath": "/pages/guide/index?shortKey=002XCUHfPi ",
        "RequestId": "49500cb4-ca5e-4da0-93fb-e15f3a710ed7 ",
        "Url": "https://essurl.cn/003hGUFil8 "
    }
}
```

