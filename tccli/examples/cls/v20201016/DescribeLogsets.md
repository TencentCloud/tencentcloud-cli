**Example 1: 获取日志集列表**

获取日志集列表

Input: 

```
tccli cls DescribeLogsets --cli-unfold-argument  \
    --Offset 0 \
    --Limit 100
```

Output: 
```
{
    "Response": {
        "Logsets": [
            {
                "LogsetId": "cce2db26-xxxx-43f3-ae7d-3502a4b424fd",
                "LogsetName": "CLS Demo日志集_100007xxxx27",
                "CreateTime": "2022-04-27 14:53:42",
                "AssumerName": "CLS",
                "Tags": [],
                "TopicCount": 8,
                "RoleName": "inner_cls_demo"
            }
        ],
        "TotalCount": 1,
        "RequestId": "141c1a10-da4b-4d86-a70d-ed49fd9b3b58"
    }
}
```

