**Example 1: 获取软件关联进程列表**



Input: 

```
tccli cwp DescribeAssetAppProcessList --cli-unfold-argument  \
    --Name xx \
    --Offset 1 \
    --Limit 1 \
    --Uuid xx \
    --Quuid xx
```

Output: 
```
{
    "Response": {
        "Process": [
            {
                "Status": "xx",
                "Name": "xx",
                "Version": "xx",
                "User": "xx",
                "StartTime": "xx",
                "Path": "xx"
            }
        ],
        "Total": 1,
        "RequestId": "xx"
    }
}
```

