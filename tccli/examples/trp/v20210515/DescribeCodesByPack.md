**Example 1: 查询码包的二维码列表**



Input: 

```
tccli trp DescribeCodesByPack --cli-unfold-argument  \
    --PackId 6w26rg8booqnjfumnu
```

Output: 
```
{
    "Response": {
        "Codes": [
            {
                "Code": "https://anxin.m.qq.com/qr/eqdmnz7020bmtvi9_008353371080418270"
            }
        ],
        "RequestId": "590de8f6-fb28-4c35-89da-e31bca7cc7ac"
    }
}
```

