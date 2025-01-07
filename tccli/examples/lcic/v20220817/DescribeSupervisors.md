**Example 1: 示例**

获取巡课列表

Input: 

```
tccli lcic DescribeSupervisors --cli-unfold-argument  \
    --SdkAppId 1 \
    --Limit 1 \
    --Page 1
```

Output: 
```
{
    "Response": {
        "Total": 1,
        "Page": 1,
        "Limit": 1,
        "UserIds": [
            "2d3FgsZRRB2EbRu5Cwe8Rd7R6Bc"
        ],
        "RequestId": "e574aae1-lp02-4225-a2f8-9032h7199f5f0"
    }
}
```

