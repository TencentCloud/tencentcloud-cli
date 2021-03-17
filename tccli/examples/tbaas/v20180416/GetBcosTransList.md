**Example 1: 获取交易列表**



Input: 

```
tccli tbaas GetBcosTransList --cli-unfold-argument  \
    --ClusterId 251005746bc987bojjue8 \
    --GroupId 1
```

Output: 
```
{
    "Response": {
        "List": [
            {
                "BlockNumber": 12,
                "BlockTimestamp": "2019-07-27 17:13:48",
                "CreateTime": "2019-07-27 10:58:04",
                "ModifyTime": "2019-07-27 10:58:04",
                "TransFrom": "0xe3726c02f48acbb2e0d1810af437d2f69af2f00d",
                "TransHash": "0xfdd42c44b46df34be8f40598a35c585d5f1eb234541d25f8e1398a0d5dc074d1",
                "TransTo": null
            },
            {
                "BlockNumber": 21,
                "BlockTimestamp": "2019-07-27 17:33:37",
                "CreateTime": "2019-07-27 10:58:12",
                "ModifyTime": "2019-07-27 10:58:12",
                "TransFrom": "0xf1585b8d0e08a0a00fff662e24d67ba95a438256",
                "TransHash": "0xf4cadb78d6cbc5b4daa42a47fafe288a448912ca662a4494817d679d54b695d8",
                "TransTo": "0x0000000000000000000000000000000000001004"
            }
        ],
        "RequestId": "d124dbd0-b0e5-4762-9ca1-37a99bd63a0f",
        "TotalCount": 2
    }
}
```

