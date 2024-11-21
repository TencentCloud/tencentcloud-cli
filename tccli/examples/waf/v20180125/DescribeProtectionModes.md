**Example 1: 查询Tiga引擎大类规则及其防护模式**

查询Tiga引擎大类规则及其防护模式

Input: 

```
tccli waf DescribeProtectionModes --cli-unfold-argument  \
    --Edition sparta-waf \
    --Domain test.domain.com
```

Output: 
```
{
    "Response": {
        "Modes": [
            {
                "Mode": 1,
                "TypeID": "010000000"
            },
            {
                "Mode": 1,
                "TypeID": "020000000"
            },
            {
                "Mode": 1,
                "TypeID": "030000000"
            },
            {
                "Mode": 1,
                "TypeID": "040000000"
            },
            {
                "Mode": 1,
                "TypeID": "050000000"
            },
            {
                "Mode": 1,
                "TypeID": "060000000"
            },
            {
                "Mode": 1,
                "TypeID": "090000000"
            },
            {
                "Mode": 1,
                "TypeID": "110000000"
            }
        ],
        "RequestId": "a73259ca-b59a-44e4-ab6d-13010a3e00ea"
    }
}
```

