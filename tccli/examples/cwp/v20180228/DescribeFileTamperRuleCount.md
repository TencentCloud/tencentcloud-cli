**Example 1: 示例**

查看主机关联多少个文件监控规则

Input: 

```
tccli cwp DescribeFileTamperRuleCount --cli-unfold-argument  \
    --Uuids 1c26308c-5493-4eaf-a817-112ec25f499e
```

Output: 
```
{
    "Response": {
        "List": [
            {
                "Count": 1,
                "Uuid": "1c26308c-5493-4eaf-a817-112ec25f499e",
                "Name": "销售许可测试机器"
            }
        ],
        "RequestId": "c741a4fd-776f-499b-85a2-7bc70fd5b92s"
    }
}
```

