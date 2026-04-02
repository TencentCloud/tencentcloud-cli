**Example 1: 获取数据目录名称列表**

获取数据目录名称列表

Input: 

```
tccli wedata ListCatalogNames --cli-unfold-argument  \
    --MaxResults 1 \
    --WorkspaceId default
```

Output: 
```
{
    "Response": {
        "Data": {
            "Items": [
                {
                    "Name": "myq_test1234",
                    "Namespace": []
                }
            ],
            "NextPageToken": "eyJvZmZzZXQiOjF9"
        },
        "RequestId": "69bff9cd-542a-4b80-86f1-351460ebe267"
    }
}
```

