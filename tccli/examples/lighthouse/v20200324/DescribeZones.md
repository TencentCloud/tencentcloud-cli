**Example 1: 查询可用区**



Input: 

```
tccli lighthouse DescribeZones --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "ZoneInfoSet": [
            {
                "Zone": "ap-guangzhou-2",
                "ZoneName": "广州二区",
                "InstanceDisplayLabel": "NORMAL"
            },
            {
                "Zone": "ap-guangzhou-3",
                "ZoneName": "广州三区",
                "InstanceDisplayLabel": "NORMAL"
            },
            {
                "Zone": "ap-guangzhou-4",
                "ZoneName": "广州四区",
                "InstanceDisplayLabel": "NORMAL"
            }
        ],
        "TotalCount": 3,
        "RequestId": "5e1bf334-e530-4c26-ab92-d911ab148d3a"
    }
}
```

