**Example 1: 可用区信息**

可用区信息

Input: 

```
tccli ocfw DescribeAllZoneList --cli-unfold-argument  \
    --CurrentAppId 1
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "Zone": "abc",
                "ZoneName": "abc"
            }
        ],
        "ReturnCode": 0,
        "ReturnMsg": "abc",
        "RequestId": "abc"
    }
}
```

