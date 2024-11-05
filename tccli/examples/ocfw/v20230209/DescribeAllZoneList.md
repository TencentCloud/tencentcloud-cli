**Example 1: 可用区信息**

可用区信息

Input: 

```
tccli ocfw DescribeAllZoneList --cli-unfold-argument  \
    --CurrentAppId 1300448058
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "Zone": "ap-guangzhou",
                "ZoneName": "广州"
            }
        ],
        "ReturnCode": 0,
        "ReturnMsg": "success",
        "RequestId": "2ddc9939-2bdc-475c-a932-ef77c7209f60"
    }
}
```

