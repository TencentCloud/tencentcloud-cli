**Example 1: 查询 clawpro 媒体库流量信息**



Input: 

```
tccli smh DescribeClawProTrafficInternal --cli-unfold-argument  \
    --LibraryId smh314*****fgfl3
```

Output: 
```
{
    "Response": {
        "LibraryId": "smh314*****fgfl3",
        "TrafficTotalBytes": 0,
        "TrafficUsedBytes": 0,
        "RequestId": "491e9e7a-fd32-47bf-b34a-e6604c4ef297"
    }
}
```

