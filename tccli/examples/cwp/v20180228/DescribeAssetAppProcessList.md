**Example 1: 获取软件关联进程列表**



Input: 

```
tccli cwp DescribeAssetAppProcessList --cli-unfold-argument  \
    --Name ssh \
    --Offset 1 \
    --Limit 1 \
    --Uuid 24c9be55-c743-4a75-a5c7-2a2912341234 \
    --Quuid 24c9be55-c743-4a75-a5c7-2a2912341234
```

Output: 
```
{
    "Response": {
        "Process": [
            {
                "Status": "S",
                "Name": "test-name",
                "Version": "0.1.1",
                "User": "root",
                "StartTime": "2024-10-11 12:23:34",
                "Path": "/root"
            }
        ],
        "Total": 1,
        "RequestId": "37b6df34-68f1-4ab8-a3d8-7b89de604c82"
    }
}
```

