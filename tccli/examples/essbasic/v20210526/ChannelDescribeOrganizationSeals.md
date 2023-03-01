**Example 1: 查询子客企业电子印章**

查询子客企业电子印章，需要操作者具有管理印章权限
客户指定需要获取的印章数量和偏移量，数量最多100，超过100按100处理；入参InfoType控制印章是否携带授权人信息，为1则携带，为0则返回的授权人信息为空数组。接口调用成功返回印章的信息列表还有企业印章的总数。

Input: 

```
tccli essbasic ChannelDescribeOrganizationSeals --cli-unfold-argument  \
    --InfoType 1 \
    --Limit 1 \
    --Agent.AppId xxxx015042c9a35e0984a9657b0ec \
    --Agent.ProxyOrganizationOpenId test1_xxxxpen_organization1 \
    --Agent.ProxyOperator.OpenId xxxtest1 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "RequestId": "8ff****2-be87-af68a7842493",
        "Seals": [
            {
                "AuthorizedUsers": [
                    {
                        "OpenId": "xxxtest1"
                    }
                ],
                "CreateOn": 163549000069,
                "Creator": "xxxtest1",
                "FailReason": "",
                "IsAllTime": true,
                "SealId": "yDxHTUUgydj94zlcUuO4zjESIzF*****",
                "SealName": "测试环境_测试",
                "SealPolicyId": "",
                "SealStatus": "SUCCESS",
                "SealType": "OFFICIAL",
                "Url": "https://***************.jpg"
            }
        ],
        "TotalCount": 35
    }
}
```

