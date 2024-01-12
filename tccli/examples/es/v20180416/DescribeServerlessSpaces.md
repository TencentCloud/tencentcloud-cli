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
                "SpaceId": "abc",
                "SpaceName": "abc",
                "Status": 0,
                "CreateTime": "abc",
                "IndexCount": 0
            }
        ],
        "RequestId": "abc"
    }
}
```

