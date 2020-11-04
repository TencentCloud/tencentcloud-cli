**Example 1: 查询个人用户配额**



Input: 

```
tccli tcr DescribeUserQuotaPersonal --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Data": {
            "LimitInfo": [
                {
                    "Username": "20548499",
                    "Type": "namespace",
                    "Value": 10
                },
                {
                    "Username": "20548499",
                    "Type": "repo",
                    "Value": 1000
                },
                {
                    "Username": "20548499",
                    "Type": "tag",
                    "Value": 1000
                }
            ]
        },
        "RequestId": "99d03fca-77f1-481f-9931-1aab2394c95a"
    }
}
```

