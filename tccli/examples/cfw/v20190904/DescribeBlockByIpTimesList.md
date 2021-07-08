**Example 1: DescribeBlockByIpTimesList**



Input: 

```
tccli cfw DescribeBlockByIpTimesList --cli-unfold-argument  \
    --Ip xx \
    --EndTime xx \
    --StartTime xx
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "StatTime": "xx",
                "Num": 0
            }
        ],
        "RequestId": "xx"
    }
}
```

