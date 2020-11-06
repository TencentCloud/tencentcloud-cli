**Example 1: DescribeBasicDeviceThreshold**



Input: 

```
tccli dayu DescribeBasicDeviceThreshold --cli-unfold-argument  \
    --BasicIp "1.1.1.1" \
    --BasicRegion "gz" \
    --BasicBizType "nat" \
    --BasicDeviceType "cvm" \
    --BasicIpInstance “aaa" \
    --BasicIspCode 5 \
    --BasicCheckFlag 1
```

Output: 
```
{
    "Response": {
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397",
        "Threshold": 10000
    }
}
```

