**Example 1: 失败示例**

请求参数不正确导致返回错误

Input: 

```
tccli partners DescribeAgentClients --cli-unfold-argument  \
    --Offset 0 \
    --Limit 0
```

Output: 
```
{
    "Response": {
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03",
        "Error": {
            "Code": "InvalidParameter",
            "Message": "Limit:0 is not int!"
        }
    }
}
```

**Example 2: 成功示例**

请求一个代理商名下代客，只取1个（Limit参数）

Input: 

```
tccli partners DescribeAgentClients --cli-unfold-argument  \
    --Offset 0 \
    --Limit 1
```

Output: 
```
{
    "Response": {
        "AgentClientSet": [
            {
                "ApplyTime": 1722396845,
                "ClientFlag": "b",
                "ClientName": "测试测试",
                "ClientUin": "2000002",
                "HasOverdueBill": 0,
                "Mail": "dadd*******@qq.com",
                "Phone": "111****0090",
                "SalesName": "testname",
                "SalesUin": "1000001",
                "Status": 1,
                "Uin": "1000002"
            }
        ],
        "TotalCount": 1,
        "RequestId": "fc90795c-1613-44e4-80ca-ce272a91d891"
    }
}
```

