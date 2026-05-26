**Example 1: 查看cos调用ua**



Input: 

```
tccli csip DescribeCosInvokeUa --cli-unfold-argument  \
    --RelAppId 1382781291
```

Output: 
```
{
    "Response": {
        "Total": 3,
        "Data": [
            "file1",
            "file2",
            "file3"
        ],
        "RequestId": "6a625df7-dea0-4ba2-9942-97303d13d23e"
    }
}
```

