**Example 1: 查询某个导播台的推流信息列表**



Input: 

```
tccli live DescribeCasterOutputInfos --cli-unfold-argument  \
    --CasterId 63501
```

Output: 
```
{
    "Response": {
        "OutputInfos": [
            {
                "OutputIndex": 0,
                "OutputType": 1,
                "OutputUrl": "rtmp://example.tlive.com/live/example_stream_id",
                "Description": "",
                "OutputStreamId": "example_stream_id",
                "OutputDomainName": "example.tlive.com",
                "OutputAppName": "live",
                "OutputParam": ""
            }
        ],
        "RequestId": "a25094ea-f516-420a-81d0-5f5c54a9e823"
    }
}
```

