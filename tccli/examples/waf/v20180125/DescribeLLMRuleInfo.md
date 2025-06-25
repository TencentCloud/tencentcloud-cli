**Example 1: 获取大模型内容检测匹配信息**

获取大模型内容检测匹配信息

Input: 

```
tccli waf DescribeLLMRuleInfo --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "InappropriateRuleList": [
            {
                "RuleId": "601",
                "RuleName": "涉政内容"
            },
            {
                "RuleId": "602",
                "RuleName": "色情内容"
            }
        ],
        "RequestId": "284bfbbd-cf39-4edc-adc6-0c1d6f2d4929",
        "SensitiveRuleList": [
            {
                "RuleId": "1",
                "RuleName": "银行卡（中国内地）"
            },
            {
                "RuleId": "3",
                "RuleName": "邮箱"
            },
            {
                "RuleId": "4",
                "RuleName": "Url"
            },
            {
                "RuleId": "5",
                "RuleName": "IP 地址"
            },
            {
                "RuleId": "6",
                "RuleName": "MAC 地址"
            },
            {
                "RuleId": "8",
                "RuleName": "手机号（中国内地）"
            },
            {
                "RuleId": "9",
                "RuleName": "固定电话（中国内地）"
            },
            {
                "RuleId": "10",
                "RuleName": "护照（中国内地）"
            },
            {
                "RuleId": "11",
                "RuleName": "家庭地址"
            },
            {
                "RuleId": "15",
                "RuleName": "身份证（中国内地）"
            },
            {
                "RuleId": "17",
                "RuleName": "车牌号码（中国内地）"
            },
            {
                "RuleId": "19",
                "RuleName": "军官证（中国内地）"
            },
            {
                "RuleId": "20",
                "RuleName": "社保卡号"
            },
            {
                "RuleId": "32",
                "RuleName": "经度"
            },
            {
                "RuleId": "33",
                "RuleName": "纬度"
            },
            {
                "RuleId": "34",
                "RuleName": "IMEI（国际移动设备识别码）"
            },
            {
                "RuleId": "36",
                "RuleName": "手机IDFA（广告标识符）"
            },
            {
                "RuleId": "37",
                "RuleName": "SK(SecretKey)"
            },
            {
                "RuleId": "39",
                "RuleName": "AK(AccessKey)"
            },
            {
                "RuleId": "44",
                "RuleName": "驾驶证（中国内地）"
            },
            {
                "RuleId": "46",
                "RuleName": "港澳通行证"
            },
            {
                "RuleId": "47",
                "RuleName": "台湾通行证"
            },
            {
                "RuleId": "48",
                "RuleName": "港澳居民来往内地通行证"
            },
            {
                "RuleId": "49",
                "RuleName": "台湾居民来往大陆通行证"
            },
            {
                "RuleId": "71",
                "RuleName": "VISA卡号"
            },
            {
                "RuleId": "72",
                "RuleName": "万事达卡号"
            },
            {
                "RuleId": "88",
                "RuleName": "IMSI（国际移动用户识别码）"
            },
            {
                "RuleId": "89",
                "RuleName": "MEID（移动设备标识符）"
            },
            {
                "RuleId": "126",
                "RuleName": "统一社会信用代码"
            },
            {
                "RuleId": "159",
                "RuleName": "车辆识别代码"
            },
            {
                "RuleId": "528",
                "RuleName": "邮政编码"
            },
            {
                "RuleId": "529",
                "RuleName": "省份代码"
            },
            {
                "RuleId": "533",
                "RuleName": "城市代码"
            },
            {
                "RuleId": "566",
                "RuleName": "微信openid"
            },
            {
                "RuleId": "572",
                "RuleName": "医保卡号"
            },
            {
                "RuleId": "573",
                "RuleName": "香港手机号码"
            }
        ]
    }
}
```

