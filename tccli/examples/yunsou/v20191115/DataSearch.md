**Example 1: 数据搜索接口**



Input: 

```
tccli yunsou DataSearch --cli-unfold-argument  \
    --NumPerPage 10 \
    --PageId 0 \
    --ResourceId 80680002 \
    --SearchId b65234af-9eb4-4e4d-a25e-d5b32c189545 \
    --SearchQuery abcde
```

Output: 
```
{
    "Response": {
        "RequestId": "f65234af-adfs-4wws-2dsa-d5b3swr575",
        "Data": {
            "CostTime": 5,
            "DisplayNum": 1,
            "Echo": "",
            "EResultNum": 1,
            "ResultList": [
                {
                    "DocAbs": "",
                    "DocId": "122",
                    "DocMeta": "{\"NC\":\"9999\",\"TD\" : \"中文\",\"NA\" : \"1000\",\"NB\" : \"9999\",\"TA\" : \"中文\",\"TB\" : \"abcde\",\"TC\" : \"中文\",\"TE\":\"tttteeee\",\"TF\":\"efeefe\",\"countrycode\":\"cn\",\"renderType\":\"rrr\"}\n",
                    "L2Score": 0
                }
            ],
            "ResultNum": 1,
            "SegList": [
                {
                    "SegStr": "abcde"
                }
            ]
        }
    }
}
```

