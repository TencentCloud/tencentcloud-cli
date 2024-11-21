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
        "RequestId": "4297c734-2f56-49d9-9c14-9d092fXXXXXX"
    }
}
```

