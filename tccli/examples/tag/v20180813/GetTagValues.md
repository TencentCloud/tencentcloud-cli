**Example 1: 查询标签值列表**



Input: 

```
tccli tag GetTagValues --cli-unfold-argument  \
    --PaginationToken CvHxL9Up8UzmIeLZKL-pSEjfF0aDNyMkn5kyTyn2M********* \
    --TagKeys key1 \
    --MaxResults 1
```

Output: 
```
{
    "Response": {
        "PaginationToken": "j5YP3W_BJau_FcWBKPPHzvDItG01rHqMuKyxW*********",
        "Tags": [
            {
                "TagKey": "key1",
                "TagValue": "value1"
            }
        ],
        "RequestId": "7337c479-d89b-4c4c-be6d-c7*********"
    }
}
```

