**Example 1: DescribeBlockByIpTimesList**



Input: 

```
tccli cfw DescribeBlockByIpTimesList --cli-unfold-argument  \
    --Ip 114.25.114.2 \
    --EndTime 2024-10-24 10:11:11 \
    --StartTime 2024-10-17 10:11:11
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "StatTime": "2024-10-17",
                "Num": 20
            }
        ],
        "RequestId": ""
    }
}
```

