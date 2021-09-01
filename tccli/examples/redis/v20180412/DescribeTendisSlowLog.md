**Example 1: 请求示例**



Input: 

```
tccli redis DescribeTendisSlowLog --cli-unfold-argument  \
    --InstanceId crs-asdasdas \
    --BeginTime '2019-09-08 12:12:41' \
    --EndTime '2019-09-09 12:12:41'
```

Output: 
```
{
    "Response": {
        "TotalCount": 106980,
        "TendisSlowLogDetail": [
            {
                "Node": "833a2f6d8b402319aee8ad7f1c0fbbf7a6604337",
                "Command": "hget",
                "CommandLine": "hget hash_key classify_scope::default",
                "Duration": 45,
                "ExecuteTime": "2019-09-08 12:13:08"
            }
        ],
        "RequestId": "121d5b40-d2b8-11e9-8c40-ef686158cbd6"
    }
}
```

