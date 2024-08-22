**Example 1: DescribeMNPApprovalList**



Input: 

```
tccli tcmpp DescribeMNPApprovalList --cli-unfold-argument  \
    --Limit 20 \
    --Offset 0 \
    --ApprovalStatusList 0 \
    --Keyword  \
    --TeamId  \
    --ApplicationId  \
    --PlatformId T04257DS9431720WTAG
```

Output: 
```
{
    "Response": {
        "Data": {
            "TotalCount": 2,
            "DataList": [
                {
                    "ApprovalNo": "aud4u4c07kp6rxiobb",
                    "ApplicationId": "app-cc6g35711m",
                    "ApprovalStatus": 0,
                    "MNPId": "mpg9yjc0qbpkelik",
                    "MNPVersion": "1.0.278",
                    "MNPVersionId": 2597,
                    "ApplyUser": "800001208871",
                    "ApplyTime": "1724142667",
                    "MNPName": "autotest_miniapp",
                    "MNPIcon": "http://127.0.0.1/T04257DS9431720WTAG/console/20240820163008-be93fce134.png",
                    "ApplicationName": "autotest_app",
                    "ApplicationLogo": "https://api.tcmpp-staging.tmfcloud.com:80/Mutable/T04257DS9431720WTAG/console/20240802112441-cf9ba6bd4c.png",
                    "TeamId": "1363731006",
                    "TeamName": "autotest_mini_team",
                    "MNPQrCodeUrl": "",
                    "MNPType": "Logistics Services->1_Pickup/Delivery,Life Service->144_Lilliputian Services",
                    "ApprovalUser": "",
                    "ApprovalTime": "0",
                    "ApprovalNote": ""
                },
                {
                    "ApprovalNo": "aud6ad75lmlbhkt4gw",
                    "ApplicationId": "app-2850c8no39",
                    "ApprovalStatus": 0,
                    "MNPId": "mp7u6lgkgphi64zo",
                    "MNPVersion": "1.0.1",
                    "MNPVersionId": 2575,
                    "ApplyUser": "vinya",
                    "ApplyTime": "1724120926",
                    "MNPName": "vinya_mini1",
                    "MNPIcon": "http://127.0.0.1/T04257DS9431720WTAG/tcmpp/20240820-595579dd-a7bd-4d98-b0ec-91ede0738c5b.png",
                    "ApplicationName": "eric_app",
                    "ApplicationLogo": "http://127.0.0.1/T04257DS9431720WTAG/console/20240819190628-466c76bda4.png",
                    "TeamId": "7681161954",
                    "TeamName": "vinya_mini",
                    "MNPQrCodeUrl": "",
                    "MNPType": "Education Services->4_Driving School Training",
                    "ApprovalUser": "",
                    "ApprovalTime": "0",
                    "ApprovalNote": ""
                }
            ]
        },
        "RequestId": "3effa0e6-397c-4d51-b6ad-7626b32013bb"
    }
}
```

