**Example 1: Querying the ID information of a district or an ISP**



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
                "Name": "China Tietong"
            }
        ],
        "ServerRegionRelation": null,
        "ClientRegionRelation": null
    }
}
```

