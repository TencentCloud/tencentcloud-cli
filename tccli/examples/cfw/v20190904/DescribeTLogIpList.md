**Example 1: DescribeTLogIpList**



Input: 

```
tccli cfw DescribeTLogIpList --cli-unfold-argument  \
    --Top 0 \
    --EndTime xx \
    --SearchValue xx \
    --QueryType xx \
    --StartTime xx
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "Ip": "xx",
                "Num": 0,
                "Port": "xx",
                "Address": "xx"
            }
        ],
        "RequestId": "xx"
    }
}
```

