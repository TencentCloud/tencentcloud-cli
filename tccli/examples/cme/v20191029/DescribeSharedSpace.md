**Example 1: 获取共享空间**



Input: 

```
tccli cme DescribeSharedSpace --cli-unfold-argument  \
    --Platform test \
    --Operator teamAmemberXXX \
    --Authorizee.Type TEAM \
    --Authorizee.Id teamA
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "AuthorizerSet": [
            {
                "Type": "PERSON",
                "Id": "abc"
            }
        ],
        "RequestId": "requestId"
    }
}
```

