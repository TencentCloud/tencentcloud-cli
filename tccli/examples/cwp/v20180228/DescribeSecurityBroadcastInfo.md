**Example 1: 查询基线详情**

根据基线id查询基线详情

Input: 

```
tccli cwp DescribeSecurityBroadcastInfo --cli-unfold-argument  \
    --Id 5
```

Output: 
```
{
    "Response": {
        "BroadcastInfo": {
            "Subtitle": "xxx",
            "Title": "xx",
            "CreateTime": "xx",
            "Content": "xx",
            "Id": 1
        },
        "RequestId": "5b49dea4-0d0e-400f-8d11-2fdf1707c51a"
    }
}
```

