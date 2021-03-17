**Example 1: 按块高查询区块信息**



Input: 

```
tccli tbaas GetBcosBlockByNumber --cli-unfold-argument  \
    --ClusterId 251005746bc987bojjue8 \
    --GroupId 0 \
    --BlockNumber 1
```

Output: 
```
{
    "Response": {
        "BlockJson": "{\"Sealer\": \"8c4affffccda617e4e16274df0e550012e94f8dcf34b2e138313bd965d08215807a90766690f6a4606f180447601d433b77a7783cfcc43b20eea7b4b5cd31eb3\", \"BlockHash\": \"0xb30403facf6f7a65150fadc00cdfe2d27d1b7b672b382175af26bcd52b552ef8\", \"BlockTimestamp\": \"2019-10-04 10:17:28\", \"BlockNumber\": 1, \"TransCount\": 1, \"ModifyTime\": \"2019-10-04 10:20:16\", \"SealerIndex\": 2, \"CreateTime\": \"2019-10-04 10:20:16\"}",
        "RequestId": "50986c54-6010-4f2e-adbe-766563597bbc"
    }
}
```

