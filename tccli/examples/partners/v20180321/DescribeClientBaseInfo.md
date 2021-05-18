**Example 1: 失败示例**

请求参数不正确导致返回错误

Input: 

```
tccli partners DescribeClientBaseInfo --cli-unfold-argument  \
    --ClientUin 10000001
```

Output: 
```
{
    "Response": {
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

**Example 2: 成功示例**

成功获取到一个代客基础信息

Input: 

```
tccli partners DescribeClientBaseInfo --cli-unfold-argument  \
    --ClientUin 1000001
```

Output: 
```
{
    "Response": {
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03",
        "ClientBaseSet": [
            {
                "AgentUin": 200000097917,
                "ClientUin": 200000098075,
                "ClientRelateType": 1,
                "AgentCooperationMode": 1,
                "AgentCountry": "US"
            }
        ],
        "TotalCount": 1
    }
}
```

