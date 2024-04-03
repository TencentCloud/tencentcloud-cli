**Example 1: 给子客企业生成签署链接**

给子客企业生成签署链接 GenerateType设置为CHANNEL, 并传子客企业的OrganizationOpenId 和子客员工的OpenId

Input: 

```
tccli essbasic CreateSignUrls --cli-unfold-argument  \
    --Agent.AppId yDwhxUUckp3gl8j5UuFX33LSNozpRsbi \
    --Agent.ProxyOrganizationOpenId org_dianziqian \
    --Agent.ProxyOperator.OpenId dianziqian \
    --Agent.ProxyAppId  \
    --FlowIds yDwiBUUckpo27hrfUuLiduRSc29fh7OX \
    --Endpoint WEIXINAPP \
    --GenerateType CHANNEL \
    --OrganizationOpenId org_zhansan \
    --OpenId n1357
```

Output: 
```
{
    "Response": {
        "SignUrlInfos": [
            {
                "SignUrl": "https://test.essurl.cn/ePXXNU8fSh",
                "Deadline": 0,
                "SignOrder": 0,
                "SignId": "",
                "CustomUserId": "",
                "Name": "",
                "Mobile": "",
                "OrganizationName": "",
                "ApproverType": "",
                "IdCardNumber": "",
                "FlowId": "yDwiBUUckpo27hrfUuLiduRSc29fh7OX",
                "OpenId": "",
                "FlowGroupId": "",
                "SignQrcodeUrl": ""
            }
        ],
        "ErrorMessages": [],
        "RequestId": "65552999-e0c6-47b7-a8db-c5e2a26b353b"
    }
}
```

**Example 2: 给所有签署人的签署链接**

给所有签署人的签署链接 GenerateType设置为ALL

Input: 

```
tccli essbasic CreateSignUrls --cli-unfold-argument  \
    --Agent.AppId yDwhxUUckp3gl8j5UuFX33LSNozpRsbi \
    --Agent.ProxyOrganizationOpenId org_zhixinlian \
    --Agent.ProxyOperator.OpenId zhixinlian \
    --Agent.ProxyAppId  \
    --FlowIds 'yDwiBUUckpo2726cUuLiduRx1WvBLD5l ' \
    --Endpoint WEIXINAPP \
    --GenerateType ALL
```

Output: 
```
{
    "Response": {
        "SignUrlInfos": [
            {
                "SignUrl": "https://test.essurl.cn/cOwbkU8fRh",
                "Deadline": 1706260744,
                "SignOrder": 0,
                "SignId": "yDwiBUUckpo2726iUuLiduRQSyCSCIK4",
                "CustomUserId": "",
                "Name": "张三",
                "Mobile": "18888888888",
                "OrganizationName": "",
                "ApproverType": "PERSON",
                "IdCardNumber": "",
                "FlowId": "yDwiBUUckpo2726cUuLiduRx1WvBLD5l ",
                "OpenId": "",
                "FlowGroupId": "",
                "SignQrcodeUrl": "https://file.test.ess.tencent.cn/bresource/resource/resource/0/0.JPG?hkey=5d92f0d***"
            },
            {
                "SignUrl": "https://test.essurl.cn/QH1dqU8eta",
                "Deadline": 1706260744,
                "SignOrder": 0,
                "SignId": "yDwiBUUckpo2726mUuLiduR8RkpoTHLy",
                "CustomUserId": "",
                "Name": "王五",
                "Mobile": "13700000000",
                "OrganizationName": "",
                "ApproverType": "ORGANIZATION",
                "IdCardNumber": "3****************3",
                "FlowId": "yDwiBUUckpo2726cUuLiduRx1WvBLD5l ",
                "OpenId": "n1379",
                "FlowGroupId": "",
                "SignQrcodeUrl": "https://file.test.ess.tencent.cn/bresource/resource/resource/0/0.JPG?hkey=5d92f0d***"
            },
            {
                "SignUrl": "https://test.essurl.cn/RaqWRU8fRg",
                "Deadline": 1706260744,
                "SignOrder": 0,
                "SignId": "yDwiBUUckpo27269UuLiduRCK7cW8oxv",
                "CustomUserId": "",
                "Name": "李四",
                "Mobile": "15100000000",
                "OrganizationName": "",
                "ApproverType": "ORGANIZATION",
                "IdCardNumber": "",
                "FlowId": "yDwiBUUckpo2726cUuLiduRx1WvBLD5l ",
                "OpenId": "",
                "FlowGroupId": "",
                "SignQrcodeUrl": "https://file.test.ess.tencent.cn/bresource/resource/resource/0/0.JPG?hkey=5d92f***"
            }
        ],
        "ErrorMessages": [
            ""
        ],
        "RequestId": "6f4198d9-2e9a-4ff7-a4f6-3ea8bd3f79ae"
    }
}
```

**Example 3: 获取动态签署人补充链接**

获取动态签署人补充链接，创建合同时未指定具体签署人，可获取链接后推送给指定的人进行补充
注： 
`1.参数GenerateType需传值为RECIPIENT` 
`2.需指定对应的签署方角色编号（即RecipientId）` 

Input: 

```
tccli essbasic CreateSignUrls --cli-unfold-argument  \
    --FlowIds yDwhGUUfe5g******CX8ZwTiSg8gISocy \
    --RecipientIds yDwJDUUckpkv98zbUEF1GNmv6ln4ga9W \
    --GenerateType RECIPIENT \
    --Agent.ProxyOrganizationOpenId 1000***8062 \
    --Agent.ProxyOperator.OpenId yDR3L****eTdCt5TVx \
    --Agent.AppId 125***319 \
    --Endpoint 
```

Output: 
```
{
    "Response": {
        "ErrorMessages": [],
        "RequestId": "s1696937862717144539",
        "SignUrlInfos": [
            {
                "ApproverType": "",
                "CustomUserId": "",
                "Deadline": 0,
                "FlowGroupId": "",
                "FlowId": "yDwhGUUfe5g******CX8ZwTiSg8gISocy",
                "IdCardNumber": "",
                "Mobile": "",
                "Name": "",
                "OpenId": "",
                "OrganizationName": "",
                "SignId": "",
                "SignOrder": 0,
                "SignQrcodeUrl": "https://file.test.ess.tencent.cn/bresource/resource/resource/0/0.JPG?hkey=5d92f0db15e6bbba6aea641f64c5c06dcbe2797f**************69ee4e24cd976dd8376dbd41c6ff227c803c4c561c",
                "SignUrl": "https://test.essurl.cn/gGI***nZC"
            }
        ]
    }
}
```

**Example 4: 给个人/自然人生成签署链接**

给个人/自然人生成签署链接 GenerateType设置为PERSON, 并传个人的名字和手机号来生成

Input: 

```
tccli essbasic CreateSignUrls --cli-unfold-argument  \
    --Agent.AppId yDwhxUUckp3gl8j5UuFX33LSNozpRsbi \
    --Agent.ProxyOrganizationOpenId org_dianziqian \
    --Agent.ProxyOperator.OpenId n9527 \
    --Agent.ProxyAppId  \
    --FlowIds yDwiBUUckpo27hh3UuLiduR83BEL3kSb \
    --Endpoint WEIXINAPP \
    --GenerateType PERSON \
    --Name 张三 \
    --Mobile 18888888888
```

Output: 
```
{
    "Response": {
        "SignUrlInfos": [
            {
                "SignUrl": "https://test.essurl.cn/9oJhnU8evP",
                "Deadline": 0,
                "SignOrder": 0,
                "SignId": "",
                "CustomUserId": "",
                "Name": "",
                "Mobile": "",
                "OrganizationName": "",
                "ApproverType": "",
                "IdCardNumber": "",
                "FlowId": "yDwiBUUckpo27hh3UuLiduR83BEL3kSb",
                "OpenId": "",
                "FlowGroupId": "",
                "SignQrcodeUrl": ""
            }
        ],
        "ErrorMessages": [],
        "RequestId": "0ec76ecb-467c-4761-8466-edb0a25bde91"
    }
}
```

**Example 5: 获取合同组动态签署人补充链接**

获取动态签署人补充链接，创建合同组时未指定具体签署人，可获取链接后推送给指定的人进行补充
注： 
`1.参数GenerateType需传值为RECIPIENT` 
`2.需指定对应的合同组FlowGroupUrlInfo签署方角色编号（即RecipientId）` 


Input: 

```
tccli essbasic CreateSignUrls --cli-unfold-argument  \
    --FlowGroupId yDCVAUUckpwa592pUxoLjOlRVS9Zgusf \
    --FlowGroupUrlInfo.FlowGroupApproverInfos.0.FlowId yDCVAUUckpwa59rcUxoLjOlEctyesTzj \
    --FlowGroupUrlInfo.FlowGroupApproverInfos.0.RecipientId yDCVAUUckpwa59riUxoLjOluu9cf6B3s \
    --FlowGroupUrlInfo.FlowGroupApproverInfos.1.FlowId yDCVAUUckpwa592dUxoLjOl8StWKvg9K \
    --FlowGroupUrlInfo.FlowGroupApproverInfos.1.RecipientId yDCVAUUckpwa59r6UxoLjOlCC6ZHk7rL \
    --GenerateType RECIPIENT \
    --Agent.ProxyOrganizationOpenId 1000***8062 \
    --Agent.ProxyOperator.OpenId yDR3L****eTdCt5TVx \
    --Agent.AppId 125***319 \
    --Endpoint 
```

Output: 
```
{
    "Response": {
        "ErrorMessages": [],
        "RequestId": "s1696937862717144539",
        "SignUrlInfos": [
            {
                "ApproverType": "",
                "CustomUserId": "",
                "Deadline": 0,
                "FlowGroupId": "",
                "FlowId": "yDwhGUUfe5g******CX8ZwTiSg8gISocy",
                "IdCardNumber": "",
                "Mobile": "",
                "Name": "",
                "OpenId": "",
                "OrganizationName": "",
                "SignId": "",
                "SignOrder": 0,
                "SignQrcodeUrl": "https://file.test.ess.tencent.cn/bresource/resource/resource/0/0.JPG?hkey=5d92f0db15e6bbba6aea641f64c5c06dcbe2797f**************69ee4e24cd976dd8376dbd41c6ff227c803c4c561c",
                "SignUrl": "https://test.essurl.cn/gGI***nZC"
            }
        ]
    }
}
```

**Example 6: 给SaaS平台企业员工签署方生成签署链接**

给SaaS平台企业员工签署方生成签署链接 GenerateType设置为NOT_CHANNEL, 并传SaaS平台企业的名称和员工的名字与手机号

Input: 

```
tccli essbasic CreateSignUrls --cli-unfold-argument  \
    --Agent.AppId yDwhxUUckp3gl8j5UuFX33LSNozpRsbi \
    --Agent.ProxyOrganizationOpenId org_dianziqian \
    --Agent.ProxyOperator.OpenId dianziqian \
    --Agent.ProxyAppId  \
    --FlowIds yDwiBUUckpo27hrfUuLiduRSc29fh7OX \
    --Endpoint WEIXINAPP \
    --GenerateType NOT_CHANNEL \
    --OrganizationName 李四示例企业 \
    --Name 李四 \
    --Mobile 15100000000
```

Output: 
```
{
    "Response": {
        "SignUrlInfos": [
            {
                "SignUrl": "https://test.essurl.cn/pr987U8euz",
                "Deadline": 1706256392,
                "SignOrder": 0,
                "SignId": "",
                "CustomUserId": "",
                "Name": "李四",
                "Mobile": "15100000000",
                "OrganizationName": "",
                "ApproverType": "ORGANIZATION",
                "IdCardNumber": "",
                "FlowId": "yDwiBUUckpo27hrfUuLiduRSc29fh7OX",
                "OpenId": "",
                "FlowGroupId": "",
                "SignQrcodeUrl": "https://file.test.ess.tencent.cn/bresource/resource/resource/0/0.JPG?hkey=5d9**2f0"
            }
        ],
        "ErrorMessages": [],
        "RequestId": "f6db6abf-512c-441f-b7e3-d17adf4a863c"
    }
}
```

**Example 7: 指定证件信息，为个人/自然人生成签署链接**

给个人/自然人生成签署链接 GenerateType设置为PERSON, 并传个人的名字、手机号和证件信息来生成

Input: 

```
tccli essbasic CreateSignUrls --cli-unfold-argument  \
    --Agent.AppId yDwhxUUckp3gl8j5UuFX33LSNozpRsbi \
    --Agent.ProxyOrganizationOpenId org_dianziqian \
    --Agent.ProxyOperator.OpenId n9527 \
    --Agent.ProxyAppId  \
    --FlowIds yDwiBUUckpo27hh3UuLiduR83BEL3kSb \
    --Endpoint WEIXINAPP \
    --GenerateType PERSON \
    --Name 张三 \
    --Mobile 18888888888 \
    --IdCardType ID_CARD \
    --IdCardNumber 620000198802020000
```

Output: 
```
{
    "Response": {
        "SignUrlInfos": [
            {
                "SignUrl": "https://essurl.cn/9oJ**P",
                "Deadline": 0,
                "SignOrder": 0,
                "SignId": "",
                "CustomUserId": "",
                "Name": "",
                "Mobile": "",
                "OrganizationName": "",
                "ApproverType": "",
                "IdCardNumber": "",
                "FlowId": "yDwiBUUckpo27hh3UuLiduR83BEL3kSb",
                "OpenId": "",
                "FlowGroupId": "",
                "SignQrcodeUrl": ""
            }
        ],
        "ErrorMessages": [],
        "RequestId": "0ec76ecb**bde91"
    }
}
```

