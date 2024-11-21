**Example 1: 获取风险服务列表**

获取风险服务列表

Input: 

```
tccli csip DescribeRiskCenterServerRiskList --cli-unfold-argument  \
    --Filter.Limit 1
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "AffectAsset": "81.**.38.139",
                "AppId": "1300448058",
                "Component": "Nginx,web",
                "FirstTime": "2024-02-18 14:56:48",
                "Id": "420e19687d33478479bf700459191135",
                "Index": "15888fd9c1ef73436cc95f04aa7b1d02",
                "InstanceId": "ins-17ye5f**",
                "InstanceName": "name",
                "InstanceType": "CVM",
                "Level": "info",
                "Nick": "天空***",
                "Port": 80,
                "Protocol": "tcp",
                "RecentTime": "2024-10-23 20:09:18",
                "RiskDetails": "detail info",
                "RiskList": [
                    {
                        "Title": "未授权访问",
                        "Body": "如果未受管理员授权，可能会被未经授权的人登录和访问"
                    },
                    {
                        "Title": "服务器被攻击",
                        "Body": " WebLogic 可能会被攻击者利用，最终导致整个服务器被攻击"
                    }
                ],
                "Service": "Nginx,web",
                "ServiceSnapshot": "https://csip-url2pic-1300616671.cos.ap-guangzhou.myqcloud.com/default/picture.png",
                "ServiceTag": "Page for the Nginx HTTP Server on  TencentOS Linux",
                "Status": 0,
                "StatusCode": "200",
                "Suggestion": "suggestion",
                "SuggestionList": [
                    {
                        "Title": "禁用未授权访问",
                        "Body": "应禁止 WebLogic 未授权的访问，通常可以通过固定的 IP 地址或者域名来做到"
                    },
                    {
                        "Title": "更新 WebLogic",
                        "Body": "WebLogic 应及时更新到最新的版本，来避免存在的漏洞被攻击者利用"
                    },
                    {
                        "Title": "定期审计",
                        "Body": "定期审计 WebLogic 的日志，可以及时发现不正常的访问行为"
                    }
                ],
                "Uin": "100011616646",
                "Url": "http://81.**.38.**:80"
            }
        ],
        "InstanceTypeLists": [
            {
                "Text": "HAVIP",
                "Value": "HAVIP"
            },
            {
                "Text": "CVM",
                "Value": "CVM"
            }
        ],
        "RequestId": "d0ae0a47-b4b9-4c55-b493-c2ffeac9b355",
        "TotalCount": 11
    }
}
```

