**Example 1: 查询互联网边界规则列表**



Input: 

```
tccli fwm DescribeEdgeAclRules --cli-unfold-argument  \
    --GroupId fwmrg-ww0m4x6493 \
    --Direction 1 \
    --Filters.0.Name SourceContent \
    --Filters.0.Values 河北 \
    --Filters.0.OperatorType 9
```

Output: 
```
{
    "Response": {
        "AllTotalCount": 52,
        "RequestId": "d33c7277-5e74-4e10-b5c7-8eea9b4cc1d8",
        "Rules": [
            {
                "CityCode": 2147483647,
                "CityKey": "hb13,sx14,ln21,jl22,hlj23,js32,zj33,ah34,fj35,jx36,sd37,hn41,hb42,hn43,gd44,hn46,sc51,gz52,yn53,sx61,gs62,qh63,nmg15,gx45,xz54,nx64,xj65,bj11,tj12,sh31,cq50",
                "CityName": "河北省,山西省,辽宁省,吉林省,黑龙江省,江苏省,浙江省,安徽省,福建省,江西省,山东省,河南省,湖北省,湖南省,广东省,海南省,四川省,贵州省,云南省,陕西省,甘肃省,青海省,内蒙古自治区,广西壮族自治区,西藏自治区,宁夏回族自治区,新疆维吾尔自治区,北京市,天津市,上海市,重庆市",
                "CloudCode": "",
                "CountryCode": 1,
                "CountryKey": "zd",
                "CountryName": "全部中国地区",
                "CreateTime": "2026-04-15 17:04:00",
                "Description": "we",
                "Direction": 1,
                "DnsParseCnt": 0,
                "InstanceName": "",
                "Invalid": 0,
                "IsCloud": 0,
                "IsRegion": 1,
                "ParamTemplateId": "",
                "ParamTemplateName": "",
                "Port": "-1/-1",
                "Protocol": "HTTPS",
                "RuleAction": "accept",
                "RuleId": "4e020c5b-d7b4-46e1-93bf-c30f1a2f8275",
                "Scope": "serial",
                "Sequence": 8,
                "SourceContent": "0.0.0.0/0",
                "SourceName": "",
                "SourceType": "net",
                "TargetContent": "qq.com",
                "TargetName": "",
                "TargetType": "domain",
                "UpdateTime": "2026-04-16 16:16:42"
            },
            {
                "CityCode": 1,
                "CityKey": "hb13",
                "CityName": "河北省",
                "CloudCode": "",
                "CountryCode": 1,
                "CountryKey": "",
                "CountryName": "",
                "CreateTime": "2026-04-15 15:59:39",
                "Description": "23",
                "Direction": 1,
                "DnsParseCnt": 0,
                "InstanceName": "",
                "Invalid": 0,
                "IsCloud": 0,
                "IsRegion": 1,
                "ParamTemplateId": "",
                "ParamTemplateName": "",
                "Port": "-1/-1",
                "Protocol": "TCP",
                "RuleAction": "accept",
                "RuleId": "91092f4e-2d8a-4f33-a53b-7a6aae6f2bd5",
                "Scope": "all",
                "Sequence": 24,
                "SourceContent": "0.0.0.0/0",
                "SourceName": "",
                "SourceType": "net",
                "TargetContent": "0.0.0.0/0",
                "TargetName": "",
                "TargetType": "net",
                "UpdateTime": "2026-04-16 16:16:42"
            }
        ],
        "TotalCount": 2
    }
}
```

