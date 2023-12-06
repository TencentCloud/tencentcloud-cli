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
                "IsEdgeOneIP": "yes",
                "Region": "中国湖南省长沙市 中国移动"
            },
            {
                "IP": "101.33.20.11",
                "IsEdgeOneIP": "yes",
                "Region": "美国California 腾讯网络"
            },
            {
                "IP": "120.222.238.33",
                "IsEdgeOneIP": "yes",
                "Region": "中国山东省青岛市 中国移动"
            },
            {
                "IP": "120.222.238.33",
                "IsEdgeOneIP": "yes",
                "Region": "中国山东省青岛市 中国移动"
            },
            {
                "IP": "120.226.17.167",
                "IsEdgeOneIP": "yes",
                "Region": "中国湖南省长沙市 中国移动"
            },
            {
                "IP": "120.226.17.168",
                "IsEdgeOneIP": "yes",
                "Region": "中国湖南省长沙市 中国移动"
            },
            {
                "IP": "43.130.34.95",
                "IsEdgeOneIP": "no",
                "Region": "美国California 腾讯网络"
            },
            {
                "IP": "43.128.224.98",
                "IsEdgeOneIP": "no",
                "Region": "日本Tokyo 腾讯网络"
            }
        ]
    }
}
```

