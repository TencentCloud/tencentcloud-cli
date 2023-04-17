**Example 1: 查询溯源信息**



Input: 

```
tccli trp DescribeTraceDataById --cli-unfold-argument  \
    --Id xfetmgoiky2nms6nk8
```

Output: 
```
{
    "Response": {
        "TraceData": {
            "Status": 0,
            "ChainStatus": 1,
            "Code": "xx",
            "PhaseData": {
                "HeadTitle": "xx",
                "AppName": "xx",
                "AppPath": "xx",
                "Key": "xx",
                "AppId": "xx",
                "HeadEnabled": true
            },
            "CorpId": 1,
            "TraceItems": [
                {
                    "Name": "xx",
                    "ReadOnly": true,
                    "Value": "xx",
                    "Ext": "xx",
                    "Values": [
                        "xx"
                    ],
                    "Key": "xx",
                    "Hidden": true,
                    "Type": "xx"
                }
            ],
            "Rank": 1,
            "CreateTime": "xx",
            "TraceId": "xx",
            "PhaseName": "xx",
            "TraceTime": "xx",
            "Phase": 1,
            "ChainData": {
                "BlockHeight": "xx",
                "BlockHash": "xx",
                "BlockTime": "xx"
            },
            "Type": 1,
            "ChainTime": "xx"
        },
        "RequestId": "xx"
    }
}
```

