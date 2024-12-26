**Example 1: test**



Input: 

```
tccli csip DescribeSubUserInfo --cli-unfold-argument  \
    --Filter.Filters.0.Name OwnerAppID \
    --Filter.Filters.0.Values 1300448058 \
    --Filter.Filters.0.OperatorType 7 \
    --Filter.Limit 10 \
    --Filter.Offset 0
```

Output: 
```
{
    "Response": {
        "CloudTypeLst": [
            {
                "Text": "腾讯云",
                "Value": "0"
            },
            {
                "Text": "亚马逊云",
                "Value": "1"
            }
        ],
        "Data": [
            {
                "ID": 54673597,
                "AppID": "1330959198",
                "Uin": "100040148813",
                "NickName": "TC_20241224_Wez4",
                "OwnerAppID": "1330***9198",
                "OwnerUin": "1000***8855",
                "OwnerNickName": "1000***78855",
                "OwnerMemberID": "mem-tencent-59de5***9af64",
                "CloudType": 0,
                "ServiceCount": 379,
                "InterfaceCount": 38408,
                "AssetCount": 1,
                "LogCount": 0,
                "ConfigRiskCount": 0,
                "ActionRiskCount": 0,
                "IsAccessCloudAudit": false,
                "IsAccessCheck": true,
                "IsAccessUeba": false
            }
        ],
        "OwnerAppIDLst": [
            {
                "Text": "天空之蓝",
                "Value": "1***448058"
            },
            {
                "Text": "xiedi勿删",
                "Value": "13***7864161"
            },
            {
                "Text": "scan勿删",
                "Value": "1317864198"
            },
            {
                "Text": "测测测",
                "Value": "131***4211"
            },
            {
                "Text": "自建账号",
                "Value": "132***38881"
            },
            {
                "Text": "1000***278855",
                "Value": "1330***198"
            },
            {
                "Text": "即用即付",
                "Value": "2229***64947"
            },
            {
                "Text": "即用即付",
                "Value": "230***9*5321"
            },
            {
                "Text": "aws-test-api-Cjhk",
                "Value": "358***6334"
            },
            {
                "Text": "TencentCSCSubAccount_20230904_7jpE4",
                "Value": "6454***52***51"
            },
            {
                "Text": "TC_20240510_J0Iz",
                "Value": "6864***15099"
            },
            {
                "Text": "TC_20240510_nZFQ",
                "Value": "792***4186"
            },
            {
                "Text": "TC_20241220_ekw3",
                "Value": "9054***53255"
            }
        ],
        "RequestId": "f711b4b6-ed7e-4cc3-8bde-9bba5732e551",
        "TotalCount": 151
    }
}
```

