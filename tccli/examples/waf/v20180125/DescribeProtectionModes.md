**Example 1: 查询Tiga引擎大类规则及其防护模式**

查询Tiga引擎大类规则及其防护模式

Input: 

```
tccli waf DescribeProtectionModes --cli-unfold-argument  \
    --Edition abc \
    --Domain abc
```

Output: 
```
{
    "Response": {
        "Modes": [
            {
                "TypeID": "abc",
                "Mode": 0
            }
        ],
        "RequestId": "abc"
    }
}
```

