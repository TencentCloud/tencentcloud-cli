**Example 1: 设置标签库**



Input: 

```
tccli wav CreateCorpTag --cli-unfold-argument  \
    --GroupName 购车计划 \
    --Sort 1 \
    --Tags.0.TagName 半年内 \
    --Tags.0.Sort 1 \
    --Tags.1.TagName 一年内 \
    --Tags.1.Sort 2 \
    --Tags.2.TagName 三年内 \
    --Tags.2.Sort 3
```

Output: 
```
{
    "Response": {
        "RequestId": "79091a0a-ee46-49bb-9c22-a070b07cbe8f",
        "TagGroup": {
            "GroupName": "购车计划",
            "BizGroupId": "1407601951281504258",
            "CreateTime": 1624433431,
            "Sort": 1,
            "Tags": [
                {
                    "TagName": "一年内",
                    "CreateTime": 1624433431,
                    "TagId": "etpqy2CAAAFrsM5y90F-pRGaiEkft--Q",
                    "Sort": 2,
                    "BizTagId": "1407601951327641602"
                },
                {
                    "TagName": "三年内",
                    "CreateTime": 1624433431,
                    "TagId": "etpqy2CAAAqgssMTUt0l_JCvml-OKY8Q",
                    "Sort": 3,
                    "BizTagId": "1407601951327641603"
                },
                {
                    "TagName": "半年内",
                    "CreateTime": 1624433431,
                    "TagId": "etpqy2CAAARruxu_UDmM5NuYkY27kBaw",
                    "Sort": 1,
                    "BizTagId": "1407601951327641601"
                }
            ],
            "GroupId": "etpqy2CAAAPp0tGn_m9B-uTiJYk7kktw"
        }
    }
}
```

