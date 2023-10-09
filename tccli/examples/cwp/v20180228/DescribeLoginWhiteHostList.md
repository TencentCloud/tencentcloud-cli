**Example 1: 编辑登录审计白名单**

编辑登录审计白名单

Input: 

```
tccli cwp DescribeLoginWhiteHostList --cli-unfold-argument  \
    --Limit 1 \
    --Id 1 \
    --Filters.0.Values xx \
    --Filters.0.Name xx \
    --Filters.0.ExactMatch True \
    --Offset 1
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "Hosts": [
            {
                "MachineName": "xx",
                "Quuid": "xx",
                "MachineWanIp": "xx",
                "Uuid": "xx",
                "MachineIp": "xx",
                "Tags": []
            }
        ],
        "RequestId": "xx"
    }
}
```

