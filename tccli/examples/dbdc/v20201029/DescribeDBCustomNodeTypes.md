**Example 1: 查询支持的节点类型**

查询当前DB Custom 支持创建的节点类型

Input: 

```
tccli dbdc DescribeDBCustomNodeTypes --cli-unfold-argument  \
    --Filters.0.Name region \
    --Filters.0.Values ap-shanghai
```

Output: 
```
{
    "Response": {
        "NodeTypeSet": [
            {
                "CPU": 512,
                "DataDiskTypes": [],
                "Memory": 2304,
                "NodeFamily": "DB.AT5",
                "NodeType": "DB.AT5.128XLARGE2304",
                "Status": "SELL",
                "SystemDiskTypes": [],
                "Zone": "ap-shanghai-5"
            }
        ],
        "RequestId": "faca34ff-e268-44f4-96e3-f7499902bd15"
    }
}
```

