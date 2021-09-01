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
                "InsID": "xx",
                "Ip": "xx",
                "InsName": "xx",
                "Num": 0,
                "Address": "xx",
                "Port": "xx"
            }
        ],
        "RequestId": "xx"
    }
}
```

