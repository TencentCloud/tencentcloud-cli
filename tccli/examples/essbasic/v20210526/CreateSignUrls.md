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

