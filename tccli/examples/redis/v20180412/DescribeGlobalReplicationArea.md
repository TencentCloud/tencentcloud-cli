**Example 1: 查询全球复制支持地域信息**

查询全球复制支持地域信息

Input: 

```
tccli redis DescribeGlobalReplicationArea --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "AvailableRegions": [
            {
                "Region": "ap-guangzhou",
                "AvailableZones": [
                    "ap-guangzhou-1"
                ]
            }
        ],
        "RequestId": "abc"
    }
}
```

