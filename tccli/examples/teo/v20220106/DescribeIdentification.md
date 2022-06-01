**Example 1: 查询站点的验证状态**



Input: 

```
tccli teo DescribeIdentification --cli-unfold-argument  \
    --Name xx
```

Output: 
```
{
    "Response": {
        "Status": "xx",
        "Name": "xx",
        "RecordType": "xx",
        "OriginalNameServers": [
            "xx"
        ],
        "RequestId": "xx",
        "Subdomain": "xx",
        "RecordValue": "xx"
    }
}
```

