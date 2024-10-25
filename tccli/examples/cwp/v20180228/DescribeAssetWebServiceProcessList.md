**Example 1: 获取Web服务关联进程列表**



Input: 

```
tccli cwp DescribeAssetWebServiceProcessList --cli-unfold-argument  \
    --Offset 1 \
    --Id 1001 \
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
                "Name": "test-name",
                "Status": "S",
                "Version": "0.1.1",
                "Path": "/root",
                "User": "root",
                "StartTime": "2024-10-11 12:23:34"
            }
        ],
        "Total": 1,
        "RequestId": "37b6df34-68f1-4ab8-a3d8-7b89de604c82"
    }
}
```

