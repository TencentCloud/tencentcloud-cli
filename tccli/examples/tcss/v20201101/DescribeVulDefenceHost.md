**Example 1: 查询漏洞防御的主机列表**

查询漏洞防御的主机列表

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
                "HostName": "abc",
                "HostIP": "abc",
                "HostID": "abc",
                "Status": "abc",
                "PublicIP": "abc",
                "CreateTime": "abc",
                "ModifyTime": "abc",
                "NodeType": "abc",
                "NodeSubNetName": "abc",
                "NodeSubNetCIDR": "abc"
            }
        ],
        "RequestId": "abc"
    }
}
```

