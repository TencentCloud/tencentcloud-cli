**Example 1: 查询异步任务**



Input: 

```
tccli clb DescribeAsyncJobs --cli-unfold-argument  \
    --RequestIds 79539486-dfe3-4be4-b9f8-f8a18bac205a \
    --NextToken eyJjdXJzb3JfaWQiOiAxfQ== \
    --MaxResults 1
```

Output: 
```
{
    "Response": {
        "Jobs": [
            {
                "ApiName": "CreateModelRouter",
                "RequestId": "f522c7e1-4913-4cc8-8672-c41b80d01164",
                "ResourceIds": [
                    "cmr-d2r861wq"
                ],
                "Status": "Processing"
            }
        ],
        "MaxResults": 1,
        "NextToken": "",
        "TotalCount": 1,
        "RequestId": "d8e86b63-069a-4844-84a7-110aeba8d4b6"
    }
}
```

