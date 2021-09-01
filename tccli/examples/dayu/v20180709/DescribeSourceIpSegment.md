**Example 1: 获取回源IP段**



Input: 

```
tccli dayu DescribeSourceIpSegment --cli-unfold-argument  \
    --Business bgpip \
    --Id bgpip-000000xe
```

Output: 
```
{
    "Response": {
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397",
        "Data": "1.1.1.0/24;2.2.2.0/24"
    }
}
```

