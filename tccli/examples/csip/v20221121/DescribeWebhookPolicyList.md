**Example 1: 示例**



Input: 

```
tccli csip DescribeWebhookPolicyList --cli-unfold-argument  \
    --Offset 0 \
    --Limit 1 \
    --Order UpdateTime \
    --By desc
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "AssetScope": {
                    "AssetRange": 1,
                    "CloudTags": [],
                    "ExcludedInstanceIds": [],
                    "InstanceIds": [],
                    "TagIds": []
                },
                "CustomFields": [],
                "ID": 5,
                "MemberId": [],
                "MsgLanguage": "zh",
                "Name": "policy1",
                "NotifyItems": [
                    {
                        "Levels": [
                            "HIGH"
                        ],
                        "Module": "Alert",
                        "SubModule": "MALWARE_FILE"
                    }
                ],
                "ReceiveFormat": "TEXT",
                "ReceiverIDList": [
                    2
                ],
                "ReceiverList": [],
                "Status": "ON"
            }
        ],
        "TotalCount": 1,
        "RequestId": "6a04ff0f-affe-4ae6-afe6-9c2f747715ba"
    }
}
```

