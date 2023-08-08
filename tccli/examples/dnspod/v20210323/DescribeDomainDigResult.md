**Example 1: 获取域名的解析结果**

获取域名的解析结果

Input: 

```
tccli dnspod DescribeDomainDigResult --cli-unfold-argument  \
    --Domain dnspod.cn \
    --RecordType A
```

Output: 
```
{
    "Response": {
        "RequestId": "f8d1eee4-f962-4e3f-8e8e-4409c4bcca0e",
        "ResultList": [
            "xx.xx.xx.xx"
        ]
    }
}
```

