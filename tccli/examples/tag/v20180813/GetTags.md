**Example 1: 查询标签列表**



Input: 

```
tccli tag GetTags --cli-unfold-argument  \
    --PaginationToken Ab9jDQQcwdAXTyU2IUabQzkIKltlrX19nJCB8MIuJD9Ck8********* \
    --MaxResults 2
```

Output: 
```
{
    "Response": {
        "PaginationToken": "t1eWpVGSKbAxvaIwRPttZIQq-Eu7e2hWKvN5iMyULmtF*********",
        "Tags": [
            {
                "TagKey": "key1",
                "TagValue": "value1"
            },
            {
                "TagKey": "key2",
                "TagValue": "value2"
            }
        ],
        "RequestId": "0ba573a8-0fdc-44eb-96d7-8f7f*********"
    }
}
```

