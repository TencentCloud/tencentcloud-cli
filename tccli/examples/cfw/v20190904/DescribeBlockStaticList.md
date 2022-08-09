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

