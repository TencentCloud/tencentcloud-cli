**Example 1: 获取安全事件列表**



Input: 

```
tccli ssa DescribeSafetyEventList --cli-unfold-argument  \
    --Filter {"FilterObj":{"Source":[],"EventType1":[],"EventType2":[],"Level":[],"Status":[],"SsaAttackChain":[],"SoarResponseStatus":[]},"Search":{"EventName":[],"AssetName":[],"AssetID":[],"AssetIpAll":[],"SrcIp":[],"DstIp":[],"SoarDagName":[]},"Id":"","Index":""} \
    --Limit 20 \
    --StartTime 2020-10-12 00:00:00 \
    --EndTime 2020-10-19 23:59:59 \
    --Offset 1 \
    --IsFilterResponseTime True
```

Output: 
```
{
    "Response": {
        "Total": 1,
        "List": [
            {
                "Index": "xx",
                "SsaDescription": "xx",
                "RuleComponents": "xx",
                "AssetName": "xx",
                "SsaEventUniqid": "xx",
                "SrcIp": "xx",
                "IsAssetDeleted": "xx",
                "SsaSrcCountry": "xx",
                "Dstport": 0,
                "Status": 1,
                "PublicIpAddresses": [
                    "xx"
                ],
                "SsaAttackChain": "xx",
                "SoarSuggestStatus": 0,
                "AssetType": "xx",
                "DstIp": "xx",
                "OldIdMd5": "xx",
                "Level": 1,
                "AssetId": "xx",
                "PrivateIpAddresses": [
                    "xx"
                ],
                "SoarResponseStatus": 0,
                "EventName": "xx",
                "Time": "2020-09-22 00:00:00",
                "EventType2": 1,
                "SoarResponseTime": 0,
                "EventType1": 1,
                "AssetIp": "xx",
                "Source": "xx",
                "AssetIpAll": [
                    "xx"
                ],
                "Id": "xx",
                "SsaDstCountry": "xx",
                "SoarPlaybookType": "xx",
                "SoarRunId": "xx",
                "SsaEventId": "xx"
            }
        ],
        "RequestId": "xx"
    }
}
```

