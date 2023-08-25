**Example 1: 查看ES的样本**

查看ES的样本数据

Input: 

```
tccli dsgc DescribeDSPAESDataSample --cli-unfold-argument  \
    --DspaId abc \
    --FieldResultId 0
```

Output: 
```
{
    "Response": {
        "Items": [
            "abc"
        ],
        "RequestId": "abc"
    }
}
```

