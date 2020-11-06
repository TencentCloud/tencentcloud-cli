**Example 1: 文档示例**



Input: 

```
tccli bizlive DescribeStreamPlayInfoList --cli-unfold-argument  \
    --PlayDomain 5000.playdomain.com \
    --StreamName stream1 \
    --StartTime '2019-03-01 00:00:00' \
    --EndTime '2019-03-01 12:00:00'
```

Output: 
```
{
    "Response": {
        "DataInfoList": [
            {
                "Time": "2019-03-01 00:00:00",
                "Bandwidth": 300.0,
                "Flux": 30.0,
                "Request": 50,
                "Online": 50
            }
        ],
        "RequestId": "8e50cdb5-56dc-408b-89b0-31818958d424"
    }
}
```

