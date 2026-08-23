**Example 1: 查询镜像木马白名单详情**



Input: 

```
tccli csip DescribeImageVirusWhitelistDetail --cli-unfold-argument  \
    --MemberId mem-12e1se11 \
    --RuleId 1
```

Output: 
```
{
    "Response": {
        "Detail": {
            "Md5List": [
                "D66D49C5242F9D4B0B2883D014AB4940"
            ],
            "OwnerAccountName": "70000*******",
            "OwnerAppId": 260000000,
            "OwnerUin": "70000*******",
            "Remark": "木马白名单",
            "RuleId": 1,
            "Scope": 1
        },
        "RequestId": "3dc013ef-bb67-4665-8890-5913d7403d6c"
    }
}
```

