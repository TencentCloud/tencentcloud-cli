**Example 1: 查询漏洞防御的主机列表**



Input: 

```
tccli tcss DescribeVulDefenceHost --cli-unfold-argument  \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "TotalCount": 0,
        "List": [
            {
                "Status": "xx",
                "ModifyTime": "xx",
                "HostName": "xx",
                "PublicIP": "xx",
                "HostIP": "xx",
                "CreateTime": "xx"
            }
        ],
        "RequestId": "xx"
    }
}
```

