**Example 1: 批量删除 DNS 记录**



Input: 

```
tccli teo DeleteDnsRecords --cli-unfold-argument  \
    --Ids xx \
    --ZoneId xx
```

Output: 
```
{
    "Response": {
        "Ids": [
            "xx"
        ],
        "RequestId": "xx"
    }
}
```

