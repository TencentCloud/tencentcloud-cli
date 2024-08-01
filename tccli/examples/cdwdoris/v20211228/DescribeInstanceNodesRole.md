**Example 1: DescribeInstanceNodesRole**

查看机器角色信息

Input: 

```
tccli cdwdoris DescribeInstanceNodesRole --cli-unfold-argument  \
    --InstanceId 1 \
    --IpFilter 1
```

Output: 
```
{
    "Response": {
        "ErrorMsg": "1",
        "NodeInfos": [
            {
                "Status": 0,
                "Ip": "1",
                "NodeRole": "1",
                "NodeName": "1"
            }
        ],
        "RequestId": "1",
        "TotalCount": 0
    }
}
```

