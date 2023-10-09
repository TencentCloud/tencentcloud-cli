**Example 1: 获取资源负载概览**



Input: 

```
tccli cwp DescribeAssetLoadInfo --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "CpuLoad": {
            "Top5": [
                {
                    "Value": 0,
                    "Desc": "xx"
                }
            ]
        },
        "MemLoad": {
            "Top5": [
                {
                    "Value": 0,
                    "Desc": "xx"
                }
            ]
        },
        "DiskLoad": {
            "Top5": [
                {
                    "Value": 0,
                    "Desc": "xx"
                }
            ]
        },
        "RequestId": "xx"
    }
}
```

