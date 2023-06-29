**Example 1: 文档示例**



Input: 

```
tccli bizlive DescribeStreamPlayInfoList --cli-unfold-argument  \
    --PlayDomain xx \
    --EndTime xx \
    --StartTime xx \
    --StreamName xx
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

