**Example 1: 拉取问答对列表**



Input: 

```
tccli icr GetIndustryV1HomeMembers --cli-unfold-argument  \
    --Payload.ID xx \
    --Metadata.AppKey xx \
    --Metadata.LBS.Latitude 0.0 \
    --Metadata.LBS.Longitude 0.0 \
    --Metadata.ChannelID xx \
    --Metadata.BusinessName xx \
    --Metadata.Vagrants.0.Value xx \
    --Metadata.Vagrants.0.Key xx \
    --Metadata.GUID xx
```

Output: 
```
{
    "Response": {
        "Payload": {
            "DataList": [
                {
                    "Status": 0,
                    "Remark": "xx",
                    "ProductList": {
                        "AppKey": "xx",
                        "Remark": "xx",
                        "Image": "xx",
                        "TemplateList": "xx",
                        "ProductName": "xx",
                        "OperatorList": "xx",
                        "CreateTime": "xx",
                        "Industry": [
                            {
                                "IndustryName": "xx",
                                "ID": "xx"
                            }
                        ],
                        "EditTime": "xx"
                    },
                    "TypeList": {
                        "TypeName": "xx",
                        "Type": "xx"
                    },
                    "FeatureList": {
                        "FeatureName": "xx",
                        "ID": "xx"
                    },
                    "MemberNum": 0,
                    "UserAccount": "xx",
                    "ID": "xx",
                    "IndustryType": "xx",
                    "EditTime": 0
                }
            ],
            "AccountLevel": "xx",
            "Total": 0,
            "Limit": 0,
            "Offset": 0
        },
        "RequestId": "xx",
        "Metadata": {
            "Message": "xx",
            "Code": 0,
            "SessionID": "xx",
            "SessionDelta": "xx"
        }
    }
}
```

