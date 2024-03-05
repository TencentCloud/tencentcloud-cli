**Example 1: 拉取设备p2p信息**

拉取设备p2p信息

Input: 

```
tccli iotvideo DescribeP2PInfo --cli-unfold-argument  \
    --ProductId KH6Q8C4N0D \
    --DeviceName aaa_31400554_1
```

Output: 
```
{
    "Response": {
        "P2PInfo": "XP2Ptest==%2.4.19",
        "ReportTime": 1708571992,
        "RequestId": "f5603714-0db6-4a4e-85a9-bb884a83a724"
    }
}
```

