**Example 1: 成功示例**

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
                "Status": 1,
                "SalesName": "xx",
                "ClientUin": "xx",
                "ClientFlag": "xx",
                "SalesUin": "xx",
                "Phone": "xx",
                "ApplyTime": 1,
                "Uin": "xx",
                "HasOverdueBill": 1,
                "Mail": "xx",
                "ClientName": "xx"
            }
        ],
        "TotalCount": 1,
        "RequestId": "xx"
    }
}
```

**Example 2: 失败示例**

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
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

