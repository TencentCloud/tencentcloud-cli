**Example 1: 获取网络攻击威胁类型列表**



Input: 

```
tccli cwp DescribeAttackVulTypeList --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "F00A8503-6233-452E-913E-DAFEE9******",
        "List": [
            "命令注入",
            "fastjson命令执行",
            "非正常的威胁类型"
        ]
    }
}
```

