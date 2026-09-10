**Example 1: 获取出站数据泄露风险事件列表**

获取出站数据泄露风险事件列表

Input: 

```
tccli cfw DescribeNDRDataLeakOutAlertList --cli-unfold-argument  \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "AnalysisStatusOptions": [
            {
                "Text": "待启动",
                "Value": "0"
            }
        ],
        "Data": [
            {
                "AiSuggestedLevel": 0,
                "AnalysisFailReason": "",
                "AnalysisStatus": 3,
                "ApiBizType": "AI推理",
                "ApiPattern": "/chat/completions",
                "Comment": "",
                "DstGeoLocation": "中国 内蒙古自治区 乌兰察布",
                "DstIPPort": "116.205.40.114:443",
                "DstServiceName": "DeepSeek",
                "DstServiceType": "ai",
                "EventCount": 3,
                "FirstIdentificationTime": "2026-03-04 10:16:05",
                "Hostname": "api.deepseek.com",
                "InstanceId": "ins-mxqs52ee",
                "InstanceName": "外联AI测试用-勿删",
                "InstanceType": "CVM",
                "LatestIdentificationTime": "2026-03-04 11:06:34",
                "LeakTypeSet": "6201,6225",
                "Level": 2,
                "Region": "ap-guangzhou",
                "RiskID": "1357473720924375000",
                "RiskScenario": "Insider Leak",
                "SrcIP": "10.0.0.10",
                "Status": 0
            }
        ],
        "DstServiceTypeOptions": [
            {
                "Text": "云存储",
                "Value": "Cloud Storage"
            }
        ],
        "InstanceTypeOptions": [
            {
                "Text": "CVM",
                "Value": "CVM"
            }
        ],
        "RegionOptions": [
            {
                "Text": "广州",
                "Value": "ap-guangzhou"
            }
        ],
        "RiskScenarioOptions": [
            {
                "Text": "批量爬取",
                "Value": "Batch Scraping"
            }
        ],
        "Total": 2,
        "RequestId": "a36e9ea4-e93b-4057-9c79-57ad91a04cef"
    }
}
```

