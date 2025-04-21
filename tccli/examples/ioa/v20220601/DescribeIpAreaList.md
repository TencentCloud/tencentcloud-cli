**Example 1: 示例1**



Input: 

```
tccli ioa DescribeIpAreaList --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Data": {
            "Page": {
                "Total": 1,
                "PageNum": 1,
                "PageSize": 10,
                "PageCount": 1
            },
            "Items": [
                {
                    "Name": "IpGroupTEst",
                    "IPConfig": "192.168.1.1",
                    "NetworkId": 3,
                    "CreateTime": "2022-11-28T15:41:52Z",
                    "EnableFlag": 1,
                    "TotalCount": 1,
                    "UpdateTime": "2022-11-28T15:41:52Z",
                    "LocationCode": "DF976814d3"
                }
            ]
        },
        "RequestId": "f96bff48-d090-464c-bffe-6ac799cb2541"
    }
}
```

