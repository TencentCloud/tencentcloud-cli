**Example 1: DescribeBlockStaticList**



Input: 

```
tccli cfw DescribeBlockStaticList --cli-unfold-argument  \
    --Top 10 \
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

