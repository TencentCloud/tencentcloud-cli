**Example 1: 查询域名详细配置**



Input: 

```
tccli teo DescribeHostsSetting --cli-unfold-argument  \
    --ZoneId xx
```

Output: 
```
{
    "Response": {
        "Hosts": [
            {
                "Status": "xx",
                "Host": "xx",
                "ZoneId": "xx",
                "AppId": 0
            }
        ],
        "RequestId": "xx",
        "TotalNumber": 0
    }
}
```

