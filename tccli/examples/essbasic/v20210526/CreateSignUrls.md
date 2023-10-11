**Example 1: 批量创建签署参与者签署H5链接**

创建链接,适用于APP或者小程序跳转

Input: 

```
tccli essbasic CreateSignUrls --cli-unfold-argument  \
    --FlowIds yDwhGUUfe5g******CX8ZwTiSg8gISocy \
    --Agent.ProxyOrganizationOpenId 1000***8062 \
    --Agent.ProxyOperator.OpenId yDR3L****eTdCt5TVx \
    --Agent.AppId 125***319 \
    --Endpoint APP
```

Output: 
```
{
    "Response": {
        "ErrorMessages": [
            ""
        ],
        "RequestId": "022cf4af-cd7a-4a53-bb94-860673a7c6dc",
        "SignUrlInfos": [
            {
                "ApproverType": "PERSON",
                "CustomUserId": "",
                "Deadline": 1722132728,
                "FlowGroupId": "",
                "FlowId": "yDwhG****iSg8gISocy",
                "IdCardNumber": "",
                "Mobile": "186****51",
                "Name": "张三",
                "OpenId": "",
                "OrganizationName": "",
                "SignId": "yDwhGUU****lVyjX8Q5w",
                "SignOrder": 0,
                "SignUrl": "pages/guide?from=default&where=mini&to=CONTRACT_DETAIL&id=yDwhGUU****ISocy&name=%E6%9D****8F%8D&phone=MTg2***Y%3D&approverVerifyTypes=1&shortKey=yDwhG***qy32"
            }
        ]
    }
}
```

**Example 2: 获取动态签署人补充链接**

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

