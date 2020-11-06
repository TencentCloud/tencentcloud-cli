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
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03",
        "AgentClientSet": [
            {
                "Uin": "100654321",
                "ClientUin": "100123456",
                "ApplyTime": "1487487666",
                "ClientFlag": "",
                "Mail": null,
                "Phone": "132****0769",
                "HasOverdueBill": 0,
                "Status": 1
            }
        ],
        "TotalCount": 20
    }
}
```

**Example 2: 失败示例**

请求参数不正确导致返回错误

Input: 

```
tccli partners DescribeAgentClients --cli-unfold-argument  \
    --Offset 0 \
    --Limit z
```

Output: 
```
{
    "Response": {
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03",
        "Error": {
            "Code": "InvalidParameter",
            "Message": "Limit:z is not int!"
        }
    }
}
```

