**Example 1: 访问日志快速分析**



Input: 

```
tccli waf DescribeAccessFastAnalysis --cli-unfold-argument  \
    --TopicId 1ae37c76-df99-4e2b-998c-20f39eba6226 \
    --From 1625395948532 \
    --To 1626000748532 \
    --Query bot:1 \
    --FieldName host
```

Output: 
```
{
    "Response": {
        "FieldValueRatioInfos": [
            {
                "Count": 4451,
                "Ratio": 0.7154798263944704,
                "Value": "bluehha.qcloudwaf.com"
            },
            {
                "Count": 1687,
                "Ratio": 0.2711782671596206,
                "Value": "qhy.17173.com"
            },
            {
                "Count": 48,
                "Ratio": 0.007715801318116058,
                "Value": "qqq323.qcloudwaf.com"
            },
            {
                "Count": 20,
                "Ratio": 0.003214917215881691,
                "Value": "0709.qcloudwaf.com"
            },
            {
                "Count": 7,
                "Ratio": 0.001125221025558592,
                "Value": "attack_log.qcloudwaf.com"
            },
            {
                "Count": 7,
                "Ratio": 0.001125221025558592,
                "Value": "bangskt.qcloudwaf.com"
            },
            {
                "Count": 1,
                "Ratio": 0.00016074586079408456,
                "Value": "zjm-mt.qcloudwaf.com"
            }
        ],
        "TotalCount": 7,
        "RequestId": "9b02bf9e-c89c-42c3-9ae1-685f968fa02d"
    }
}
```

