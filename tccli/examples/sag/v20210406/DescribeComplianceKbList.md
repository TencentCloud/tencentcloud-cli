**Example 1: 获取合规补丁列表**



Input: 

```
tccli sag DescribeComplianceKbList --cli-unfold-argument  \
    --Os Windows \
    --Offset 1 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "Total": 100,
        "List": [
            {
                "Kb": "KB2207566",
                "Desc": "现已确认有一个安全问题，未通过身份验证的远程攻击者可能会利用此问题导致受影响的系统停止响应。",
                "PubTime": "2010.10.25"
            }
        ],
        "RequestId": "xxx"
    }
}
```

