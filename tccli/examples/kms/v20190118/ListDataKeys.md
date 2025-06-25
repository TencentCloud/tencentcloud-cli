**Example 1: 获取数据密钥列表示例**

获取数据密钥

Input: 

```
tccli kms ListDataKeys --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "DataKeys": [
            {
                "DataKeyId": "50cc8e9f-4f44-11f0-ace9-525400eb1719"
            },
            {
                "DataKeyId": "32e9bd2c-4f44-11f0-ace9-525400eb1719"
            },
            {
                "DataKeyId": "d02ea923-4f43-11f0-b672-52540073b995"
            },
            {
                "DataKeyId": "1a6a8465-4dc8-11f0-b672-52540073b995"
            },
            {
                "DataKeyId": "f3fd3a12-4dba-11f0-ace9-525400eb1719"
            },
            {
                "DataKeyId": "d6e6cf2d-4ceb-11f0-8428-52540073b995"
            },
            {
                "DataKeyId": "c0fb30d1-4ceb-11f0-bcaa-525400eb1719"
            },
            {
                "DataKeyId": "72da485a-4ceb-11f0-bcaa-525400eb1719"
            },
            {
                "DataKeyId": "602b4824-4ceb-11f0-bcaa-525400eb1719"
            },
            {
                "DataKeyId": "52293da7-4cc1-11f0-a29a-525400eb1719"
            }
        ],
        "RequestId": "e9033eb2-e7ba-46a6-b83e-3bc2fc8d906c",
        "TotalCount": 132
    }
}
```

