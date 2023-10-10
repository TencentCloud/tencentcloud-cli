**Example 1: 获取主机磁盘列表**



Input: 

```
tccli cwp DescribeAssetDiskList --cli-unfold-argument  \
    --Offset 1 \
    --Limit 1 \
    --Uuid xx \
    --Quuid xx
```

Output: 
```
{
    "Response": {
        "Disks": [
            {
                "Path": "xx",
                "Type": "xx",
                "Percent": 0.0,
                "Name": "xx",
                "Size": 1
            }
        ],
        "RequestId": "xx",
        "Total": 1
    }
}
```

