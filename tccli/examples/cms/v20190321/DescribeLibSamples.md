**Example 1: 获取关键词接口**

获取关键词

Input: 

```
tccli cms DescribeLibSamples --cli-unfold-argument  \
    --LibID abc \
    --Limit 0 \
    --Offset 0 \
    --Content abc \
    --EvilTypeList 0 \
    --SampleIDs 123 456
```

Output: 
```
{
    "Response": {
        "TotalCount": 0,
        "Infos": [
            {
                "ID": "abc",
                "Content": "abc",
                "Label": "abc",
                "CreateTime": "abc",
                "Remark": "abc",
                "WordType": "abc"
            }
        ],
        "RequestId": "abc"
    }
}
```

