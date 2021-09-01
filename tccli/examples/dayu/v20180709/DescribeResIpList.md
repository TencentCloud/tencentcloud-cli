**Example 1: 获取资源的IP列表**



Input: 

```
tccli dayu DescribeResIpList --cli-unfold-argument  \
    --Business bgpip \
    --Id bgpip-000000xe
```

Output: 
```
{
    "Response": {
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397",
        "Resource": [
            {
                "Id": "bgpip-000000xe",
                "IpList": [
                    "1.1.1.1"
                ]
            }
        ]
    }
}
```

