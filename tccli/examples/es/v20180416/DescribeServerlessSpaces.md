**Example 1: 获取Serverless索引空间列表**



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
                "Status": 0,
                "SpaceName": "xx",
                "SpaceId": "xx",
                "CreateTime": "xx"
            }
        ],
        "RequestId": "xx"
    }
}
```

