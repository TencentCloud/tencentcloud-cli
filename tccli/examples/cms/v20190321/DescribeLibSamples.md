**Example 1: 获取关键词接口**

获取关键词

Input: 

```
tccli cms DescribeLibSamples --cli-unfold-argument  \
    --Type text \
    --UserAppID 11234 \
    --UserUin 11223344 \
    --UserSubUin 11223344 \
    --LibID xxx-xxx-xxx \
    --Limit 0 \
    --Offset 0 \
    --Content keyword \
    --EvilTypeList 0 \
    --SampleIDs 23231 45236
```

Output: 
```
{
    "Response": {
        "TotalCount": 0,
        "Infos": [
            {
                "ID": "xxx-xxx-xxx",
                "Content": "keyword",
                "Label": "Normal",
                "CreateTime": "2012-01-02 15:04:05:06",
                "Remark": "remark",
                "WordType": "Default"
            }
        ],
        "RequestId": "xxxx-xxxxx-xxxx"
    }
}
```

