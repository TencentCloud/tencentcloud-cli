**Example 1: 查询安全播报文章信息**

根据id查询安全播报文章信息

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
            "Subtitle": "安全播报",
            "Title": "安全播报",
            "CreateTime": "2019-12-25 11:57:15",
            "Content": "安全播报",
            "Id": 5
        },
        "RequestId": "5b49dea4-0d0e-400f-8d11-2fdf1707c51a"
    }
}
```

