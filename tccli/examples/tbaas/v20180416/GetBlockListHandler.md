**Example 1: 查询区块列表**



Input: 

```
tccli tbaas GetBlockListHandler --cli-unfold-argument  \
    --Module block \
    --Operation get_block_list \
    --Offset 0 \
    --Limit 4 \
    --GroupPk 11_1 \
    --BlockHash 0
```

Output: 
```
{
    "Response": {
        "GroupPk": "11_1",
        "List": [
            {
                "BlockHash": "0xb30403facf6f7a65150fadc00cdfe2d27d1b7b672b382175af26bcd52b552ef8",
                "BlockNumber": 1,
                "BlockTimestamp": "2019-10-04 10:17:28",
                "CreateTime": "2019-10-04 10:20:16",
                "ModifyTime": "2019-10-04 10:20:16",
                "Sealer": "8c4affffccda617e4e16274df0e550012e94f8dcf34b2e138313bd965d08215807a90766690f6a4606f180447601d433b77a7783cfcc43b20eea7b4b5cd31eb3",
                "SealerIndex": 2,
                "TransCount": 1
            },
            {
                "BlockHash": "0x6ae08948b5c0385a0393f688271291b5806edce462eb67a8382528a6d757e525",
                "BlockNumber": 0,
                "BlockTimestamp": "2019-10-03 22:31:52",
                "CreateTime": "2019-10-03 22:34:57",
                "ModifyTime": "2019-10-03 22:34:57",
                "Sealer": "388a58a628c3dbb2aba593c7dc557ac36d386e931f15049ad8c5a3b2ea253e3edf25ccc80ac3012b6b78534889255cee2ac6f9b2dac80b47f75b52be0e4e8bb3",
                "SealerIndex": 0,
                "TransCount": 0
            }
        ],
        "RequestId": "d124dbd0-b0e5-4762-9ca1-37a99bd63a0f",
        "TotalCount": 2
    }
}
```

