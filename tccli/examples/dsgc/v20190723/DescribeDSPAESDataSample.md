**Example 1: 查看ES的样本**

查看ES的样本数据

Input: 

```
tccli dsgc DescribeDSPAESDataSample --cli-unfold-argument  \
    --DspaId dspa-2nksd3as \
    --FieldResultId 10
```

Output: 
```
{
    "Response": {
        "Items": [
            "武汉市",
            "北京市",
            "上海市",
            "广州市",
            "深圳市",
            "成都市",
            "杭州市"
        ],
        "RequestId": "5b208867-7b62-4932-ac72-95a5b38f80ec"
    }
}
```

