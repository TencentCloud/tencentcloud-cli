**Example 1: 获取CC四层黑白名单列表**



Input: 

```
tccli antiddos DescribeCcBlackWhiteIpList --cli-unfold-argument  \
    --Domain xx \
    --Protocol xx \
    --Business xx \
    --InstanceId xx \
    --Ip xx \
    --Limit 1 \
    --Offset 1
```

Output: 
```
{
    "Response": {
        "Total": 1,
        "CcBlackWhiteIpList": [
            {
                "Domain": "xx",
                "BlackWhiteIp": "xx",
                "Protocol": "xx",
                "InstanceId": "xx",
                "Ip": "xx",
                "Mask": 1,
                "PolicyId": "xx",
                "ModifyTime": "xx",
                "Type": "xx",
                "CreateTime": "xx"
            }
        ],
        "RequestId": "xx"
    }
}
```

