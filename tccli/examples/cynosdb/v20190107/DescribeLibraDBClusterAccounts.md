**Example 1: 查询分析集群账号**



Input: 

```
tccli cynosdb DescribeLibraDBClusterAccounts --cli-unfold-argument  \
    --ClusterId libradb-i794jfvg
```

Output: 
```
{
    "Response": {
        "AccountSet": [
            {
                "AccountName": "root",
                "CreateTime": "2025-12-25 16:20:05",
                "Description": "",
                "Host": "%",
                "MaxUserConnections": 0,
                "UpdateTime": "2025-12-25 16:22:41"
            }
        ],
        "TotalCount": 2,
        "RequestId": "353a315c-71c3-4a39-a5d8-c1055f1f176d"
    }
}
```

