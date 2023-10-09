**Example 1: 示例**

查看主机关联多少个文件监控规则

Input: 

```
tccli cwp DescribeFileTamperRuleCount --cli-unfold-argument  \
    --Uuids xx
```

Output: 
```
{
    "Response": {
        "List": [
            {
                "Count": 1,
                "Uuid": "xx",
                "Name": "xx"
            }
        ],
        "RequestId": "c741a4fd-776f-499b-85a2-7bc70fd5b92s"
    }
}
```

