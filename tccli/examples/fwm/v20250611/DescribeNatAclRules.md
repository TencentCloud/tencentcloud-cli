**Example 1: 查询 NAT 规则列表**



Input: 

```
tccli fwm DescribeNatAclRules --cli-unfold-argument  \
    --GroupId fwmrg_9tnz3ksn7v \
    --Direction 0 \
    --Filters.0.Name TargetContent \
    --Filters.0.Values 河北省 \
    --Filters.0.OperatorType 9
```

Output: 
```
{
    "Response": {
        "AllTotalCount": 10,
        "RequestId": "23fd42d9-7a67-4a0a-b6f1-e598451d798d",
        "Rules": [
            {
                "CityCode": 2146303999,
                "CityKey": "hb13,sx14,ln21,jl22,hlj23,js32,zj33,ah34,fj35,jx36,sd37,hn41,hb42,hn43,gd44,hn46,sc51,yn53,sx61,qh63,nmg15,gx45,xz54,nx64,xj65,bj11,tj12,sh31,cq50",
                "CityName": "河北省,山西省,辽宁省,吉林省,黑龙江省,江苏省,浙江省,安徽省,福建省,江西省,山东省,河南省,湖北省,湖南省,广东省,海南省,四川省,云南省,陕西省,青海省,内蒙古自治区,广西壮族自治区,西藏自治区,宁夏回族自治区,新疆维吾尔自治区,北京市,天津市,上海市,重庆市",
                "CountryCode": 1,
                "CreateTime": "2026-04-02 17:16:53",
                "Description": "3412",
                "Direction": 0,
                "DnsParseCnt": 0,
                "IsRegion": 1,
                "ParamTemplateId": "",
                "ParamTemplateName": "",
                "Port": "-1/-1",
                "Protocol": "ANY",
                "RuleAction": "accept",
                "RuleId": "ba37feba-4ff5-46c7-b876-77bbc456cdc7",
                "Scope": "ALL",
                "ScopeDesc": "全局规则",
                "Sequence": 8,
                "SourceContent": "43.143.218.25",
                "SourceType": "net",
                "TargetContent": "0.0.0.0/0",
                "TargetType": "net",
                "UpdateTime": "2026-04-07 18:15:05"
            }
        ],
        "TotalCount": 1
    }
}
```

