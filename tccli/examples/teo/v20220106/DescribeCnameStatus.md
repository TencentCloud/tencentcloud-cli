**Example 1: 查询域名 CNAME 状态**



Input: 

```
tccli teo DescribeCnameStatus --cli-unfold-argument  \
    --Names xx \
    --ZoneId xx
```

Output: 
```
{
    "Response": {
        "Status": [
            {
                "Status": "xx",
                "Cname": "xx",
                "Name": "xx"
            }
        ],
        "RequestId": "xx"
    }
}
```

