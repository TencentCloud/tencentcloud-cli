**Example 1: 获取应用对应sourcemap文件列表**

获取应用对应sourcemap文件列表

Input: 

```
tccli rum DescribeReleaseFiles --cli-unfold-argument  \
    --ProjectID '1

{
  "ProjectID": 2,
  "FileName": "2"
}'
```

Output: 
```
{
    "Response": {
        "Files": [
            {
                "Version": "0.01",
                "FileKey": "****test",
                "FileName": "a.js.map",
                "FileHash": "****test"
            }
        ],
        "RequestId": "65a8fec7-2b39-4b11-893f-3715279d235f"
    }
}
```

