**Example 1: 按主题名模糊查询**

按名称模糊查询日志主题

Input: 

```
tccli dlc DescribeClsTopics --cli-unfold-argument  \
    --TopicName ray \
    --Offset 0 \
    --Limit 20
```

Output: 
```
{
    "Response": {
        "TotalCount": 2,
        "Topics": [
            {
                "TopicId": "acec1e06-8877-4e9d-9472-7247a45ae57f",
                "TopicName": "ray-nexus"
            },
            {
                "TopicId": "79f26370-b30e-44c5-9cb2-1eb7c202a9aa",
                "TopicName": "neutrino-resourcemanager"
            }
        ],
        "RequestId": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
    }
}
```

