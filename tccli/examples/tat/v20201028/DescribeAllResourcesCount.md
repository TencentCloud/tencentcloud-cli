**Example 1: 查询所有地域下指定资源的数量**



Input: 

```
tccli tat DescribeAllResourcesCount --cli-unfold-argument  \
    --ResourceNames COMMAND
```

Output: 
```
{
    "Response": {
        "TotalCount": 2,
        "RegionResourceCountSet": [
            {
                "Region": "ap-guangzhou",
                "ResourceCountDetailSet": [
                    {
                        "ResourceName": "COMMAND",
                        "ResourceCount": 20
                    }
                ]
            },
            {
                "Region": "ap-hongkong",
                "ResourceCountDetailSet": [
                    {
                        "ResourceName": "COMMAND",
                        "ResourceCount": 9
                    }
                ]
            }
        ],
        "RequestId": "7660ce41-d33e-40af-a814-43d9ea62d59b"
    }
}
```

