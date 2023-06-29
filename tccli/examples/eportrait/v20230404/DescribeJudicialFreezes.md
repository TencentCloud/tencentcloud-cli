**Example 1: DescribeJudicialFreezes1**

DescribeJudicialFreezes1

Input: 

```
tccli eportrait DescribeJudicialFreezes --cli-unfold-argument  \
    --Eid 00039d63a5a7855713ac03f99a91be57 \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "Amount": "319万人民币",
                "BeExecutedPerson": "云南阳光基业能源管控技术股份有限公司",
                "Detail": null,
                "ExecutiveCourt": "昆明市呈贡区人民法院",
                "LoseEfficacyDate": null,
                "LoseEfficacyReason": null,
                "Number": "（2018）云0114执1302号",
                "PcFreezeDetail": {
                    "ExecuteDate": "2019-04-09"
                },
                "Type": "股权变更",
                "UnFreezeDetails": null
            }
        ],
        "RequestId": "de1b91eb-cd98-4ef8-aadf-51fd429be739",
        "TotalCount": 1
    }
}
```

