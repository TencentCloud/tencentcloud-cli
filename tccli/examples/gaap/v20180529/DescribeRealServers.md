**Example 1: 查询源站信息**



Input: 

```
tccli gaap DescribeRealServers --cli-unfold-argument  \
    --ProjectId 0 \
    --SearchValue '1.1.1.1'
```

Output: 
```
{
    "Response": {
        "RealServerSet": [
            {
                "RealServerId": "rs123",
                "RealServerIP": "1.1.1.1",
                "RealServerName": "rsname",
                "ProjectId": 0,
                "TagSet": []
            }
        ],
        "TotalCount": 1,
        "RequestId": "5c680029-66b2-4be8-9630-7bd316ce70dd"
    }
}
```

