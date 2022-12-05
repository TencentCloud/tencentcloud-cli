**Example 1: 获取CC四层黑白名单列表**



Input: 

```
tccli antiddos DescribeCcBlackWhiteIpList --cli-unfold-argument  \
    --Domain www.test1.com \
    --Protocol https \
    --Business bgpip \
    --InstanceId bgpip-000000z9 \
    --Ip 1.1.1.1 \
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
                "Domain": "www.test1.com",
                "BlackWhiteIp": "2.2.2.2",
                "Protocol": "https",
                "InstanceId": "bgpip-000004z9",
                "Ip": "1.1.1.1",
                "Mask": 1,
                "PolicyId": "ccBlackWhite-000002s7",
                "ModifyTime": "2022-04-30 08:09:20",
                "Type": "white",
                "CreateTime": "2022-04-30 07:09:20"
            }
        ],
        "RequestId": "1be9f39c-7060-11ed-aae2-525400f921f0"
    }
}
```

