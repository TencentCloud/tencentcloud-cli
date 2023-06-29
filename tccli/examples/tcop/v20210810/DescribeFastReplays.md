**Example 1: 获取直播课回放列表**

该API获取一门直播课的回放列表

Input: 

```
tccli tcop DescribeFastReplays --cli-unfold-argument  \
    --IdaasOrgId tn-c65190017f394836863e83ca429b500c \
    --TermId 1000030510 \
    --Page 1 \
    --PageSize 10
```

Output: 
```
{
    "Response": {
        "PageNext": 100,
        "ReplayList": [
            {
                "Name": "第一讲",
                "VId": "1628843523",
                "TaskId": "1",
                "Timelen": "3600"
            }
        ],
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

