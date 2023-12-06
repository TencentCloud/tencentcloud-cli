**Example 1: 查询IP地理位置归属信息**



Input: 

```
tccli teo DescribeIPRegion --cli-unfold-argument  \
    --IPs 1.1.1.1 2402:4e00:1403:eb00:0:9440:b55a:39a8
```

Output: 
```
{
    "Response": {
        "RequestId": "bc0bb357-0b72-4abb-ae66-ffffb965aced",
        "IPRegionInfo": [
            {
                "IP": "120.226.17.168",
                "IsEdgeOneIP": "yes"
            },
            {
                "IP": "101.33.20.11",
                "IsEdgeOneIP": "yes"
            },
            {
                "IP": "120.222.238.33",
                "IsEdgeOneIP": "yes"
            },
            {
                "IP": "120.222.238.33",
                "IsEdgeOneIP": "yes"
            },
            {
                "IP": "120.226.17.167",
                "IsEdgeOneIP": "yes"
            },
            {
                "IP": "120.226.17.168",
                "IsEdgeOneIP": "yes"
            },
            {
                "IP": "43.130.34.95",
                "IsEdgeOneIP": "no"
            },
            {
                "IP": "43.128.224.98",
                "IsEdgeOneIP": "no"
            }
        ]
    }
}
```

