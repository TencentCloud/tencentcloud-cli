**Example 1: 查询所有区块列表**



Input: 

```
tccli tbaas GetBlockList --cli-unfold-argument  \
    --Module block \
    --Operation block_list \
    --ChannelId 0 \
    --GroupId 0 \
    --ChannelName kylotst \
    --GroupName liulanOrg \
    --ClusterId 251005746bc0f03q8u93j \
    --Offset 0 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "BlockList": [
            {
                "BlockId": 5,
                "BlockNum": 5,
                "DataHash": "92f1c3b1eb0eb1bc1825f1acd3474e7679b2a97cdf8d6155ed6a0e6c1458e479",
                "PreHash": "92f1c3b1eb0eb1bc1825f1acd3474e7679b2a97cdf8d6155ed6a0e6c1458e479",
                "TxCount": 1
            },
            {
                "BlockId": 4,
                "BlockNum": 4,
                "DataHash": "17e381e65605963c9211abc5b72d80cf3a6a4955ff7b61c70b406b98c90ded6f",
                "PreHash": "17e381e65605963c9211abc5b72d80cf3a6a4955ff7b61c70b406b98c90ded6f",
                "TxCount": 1
            },
            {
                "BlockId": 3,
                "BlockNum": 3,
                "DataHash": "32b80e93141467eda367f05a2428a6c03369405ae10349db7fad0762e9b56cc2",
                "PreHash": "32b80e93141467eda367f05a2428a6c03369405ae10349db7fad0762e9b56cc2",
                "TxCount": 1
            },
            {
                "BlockId": 2,
                "BlockNum": 2,
                "DataHash": "8be5094bf40c5b7e410cc3e8aa33354da2aa78db862e17cfd5fa783dddc1ee3a",
                "PreHash": "8be5094bf40c5b7e410cc3e8aa33354da2aa78db862e17cfd5fa783dddc1ee3a",
                "TxCount": 1
            },
            {
                "BlockId": 1,
                "BlockNum": 1,
                "DataHash": "af319fe2ff9e5830af0f07200adf965156446a205137e61d87f1db0b8f43cc7e",
                "PreHash": "af319fe2ff9e5830af0f07200adf965156446a205137e61d87f1db0b8f43cc7e",
                "TxCount": 1
            },
            {
                "BlockId": 0,
                "BlockNum": 0,
                "DataHash": "96f22d00947478c1b16c2aec5e7079c761b168d304cadf19a14a032ee8f64a23",
                "PreHash": "96f22d00947478c1b16c2aec5e7079c761b168d304cadf19a14a032ee8f64a23",
                "TxCount": 1
            }
        ],
        "RequestId": "018328c8-9c24-4104-a0ad-a7a31c033278",
        "TotalCount": 6
    }
}
```

