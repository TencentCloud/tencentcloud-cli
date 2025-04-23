**Example 1: 获取Serverless索引空间列表**

获取Serverless索引空间列表

Input: 

```
tccli es DescribeServerlessSpaces --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "TotalCount": 0,
        "ServerlessSpaces": [
            {
                "SpaceId": "space-eafhiefi",
                "SpaceName": "spaceName",
                "Status": 1,
                "CreateTime": "2024-12-11 17:50:05",
                "IndexCount": 1
            }
        ],
        "RequestId": "40f4f780-9969-42f9-8bd9-ccf0d1f2591a"
    }
}
```

