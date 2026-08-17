**Example 1: 查看容灾盘信息**



Input: 

```
tccli bdrc DescribeDisks --cli-unfold-argument  \
    --DiskIds disk-a8ys45xk \
    --DiskRegion ap-guangzhou
```

Output: 
```
{
    "Response": {
        "DiskInfoSet": [
            {
                "DiskId": "disk-a8ys45xk",
                "ImageFormat": "RAW"
            }
        ],
        "TotalCount": 1,
        "RequestId": "3a9f90a2-3841-43ce-880e-4bd1bee5a335"
    }
}
```

