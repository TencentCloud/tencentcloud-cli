**Example 1: 查询溯源信息**



Input: 

```
tccli trp DescribeTraceDataList --cli-unfold-argument  \
    --BatchId xfetmgoiky2nms6nk8 \
    --Code  \
    --PageSize 10 \
    --PageNumber 1
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "TraceDataList": [
            {
                "Type": 1,
                "ChainStatus": 1,
                "Code": "xx",
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
                        "Hidden": true,
                        "Type": "xx"
                    }
                ],
                "Rank": 1,
                "TraceId": "xx",
                "PhaseName": "xx",
                "TraceTime": "xx",
                "Phase": 1,
                "ChainData": {
                    "BlockHeight": 1,
                    "BlockHash": "xx"
                },
                "ChainTime": "xx",
                "CreateTime": "xx"
            }
        ],
        "RequestId": "xx"
    }
}
```

