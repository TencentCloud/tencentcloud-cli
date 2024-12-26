**Example 1: 查询导播台展示信息**



Input: 

```
tccli live DescribeCasterDisplayInfo --cli-unfold-argument  \
    --CasterId 63501
```

Output: 
```
{
    "Response": {
        "PvwDisplayInfo": {
            "LayoutIndex": 0,
            "MarkPicIndexList": [],
            "MarkWordIndexList": [],
            "TransitionType": "",
            "AudioIndexList": []
        },
        "PgmDisplayInfo": {
            "LayoutIndex": 0,
            "MarkPicIndexList": [],
            "MarkWordIndexList": [],
            "TransitionType": "",
            "AudioIndexList": []
        },
        "Status": 0,
        "RequestId": "uuid",
        "StartLiveTime": 1670309219
    }
}
```

