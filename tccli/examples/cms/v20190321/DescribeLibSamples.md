**Example 1: 获取关键词接口**



Input: 

```
tccli cms DescribeLibSamples --cli-unfold-argument  \
    --UserAppID xx \
    --UserSubUin xx \
    --Content xx \
    --EvilTypeList 0 \
    --LibID xx \
    --Limit 0 \
    --Offset 0 \
    --UserUin xx \
    --Type xx
```

Output: 
```
{
    "Response": {
        "TotalCount": 3000,
        "Infos": [
            {
                "Content": "xx",
                "ID": "xx",
                "CreateTime": "xx",
                "Label": "xx"
            }
        ],
        "RequestId": "xx"
    }
}
```

