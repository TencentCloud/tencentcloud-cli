**Example 1: 获取基础防护CC防护阈值**



Input: 

```
tccli dayu DescribeBasicCCThreshold --cli-unfold-argument  \
    --BasicIp "1.1.1.1" \
    --BasicRegion "gz" \
    --BasicBizType "nat" \
    --BasicDeviceType "cvm" \
    --BasicIpInstance “aaa" \
    --BasicIspCode 5
```

Output: 
```
{
    "Response": {
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397",
        "CCEnable": 1,
        "CCThreshold": 100
    }
}
```

