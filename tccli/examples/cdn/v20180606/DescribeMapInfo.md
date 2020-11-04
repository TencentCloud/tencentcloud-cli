**Example 1: 查询省份/运营商映射关系**



Input: 

```
tccli cdn DescribeMapInfo --cli-unfold-argument  \
    --Name isp
```

Output: 
```
{
    "Response": {
        "RequestId": "fcd7aded-1866-467e-a9f6-d8d00b09557e",
        "MapInfoList": [
            {
                "Id": 3947,
                "Name": "中国铁通"
            }
        ],
        "ServerRegionRelation": null,
        "ClientRegionRelation": null
    }
}
```

