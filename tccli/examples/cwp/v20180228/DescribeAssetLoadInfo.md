**Example 1: 获取资源负载概览**



Input: 

```
tccli cwp DescribeAssetLoadInfo --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "CpuLoad": {
            "Counts": [
                1
            ],
            "Top5": [
                {
                    "MachineName": "instance-1",
                    "Desc": "idesc",
                    "Value": 0,
                    "Quuid": "24c9be55-c743-4a75-a5c7-2a2912341234",
                    "Uuid": "24c9be55-c743-4a75-a5c7-2a2912341234"
                }
            ]
        },
        "MemLoad": {
            "Counts": [
                1
            ],
            "Top5": [
                {
                    "MachineName": "instance-12",
                    "Desc": "idesc",
                    "Value": 0,
                    "Quuid": "24c9be55-c743-4a75-a5c7-2a2912341234",
                    "Uuid": "24c9be55-c743-4a75-a5c7-2a2912341234"
                }
            ]
        },
        "DiskLoad": {
            "Counts": [
                1
            ],
            "Top5": [
                {
                    "MachineName": "instance-13",
                    "Desc": "idesc",
                    "Value": 0,
                    "Quuid": "24c9be55-c743-4a75-a5c7-2a2912341234",
                    "Uuid": "24c9be55-c743-4a75-a5c7-2a2912341234"
                }
            ]
        },
        "RequestId": "24c9be55-c743-4a75-a5c7-2a2912341234"
    }
}
```

