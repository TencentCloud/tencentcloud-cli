**Example 1: 请求示例**



Input: 

```
tccli live DescribeLiveXP2PDetailInfoList --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "DataInfoList": [
            {
                "StuckTimes": 0,
                "StreamName": "xx",
                "Request": 2405,
                "RequestSuccess": 0,
                "AppId": "xx",
                "CdnBytes": 386806176036,
                "P2pBytes": 299529921749,
                "OnlinePeople": 61854,
                "Time": "xx",
                "Type": "xx",
                "StuckPeople": 1177
            },
            {
                "Time": "xx",
                "StuckTimes": 0,
                "StreamName": "xx",
                "Request": 885,
                "CdnBytes": 257972842317,
                "RequestSuccess": 0,
                "P2pBytes": 120206082328,
                "OnlinePeople": 35038,
                "AppId": "xx",
                "Type": "xx",
                "StuckPeople": 2246
            }
        ],
        "RequestId": "xx"
    }
}
```

