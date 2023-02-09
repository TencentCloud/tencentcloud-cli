**Example 1: 查询号码列表**

查询号码列表

Input: 

```
tccli ccc DescribeNumbers --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "Numbers": [
            {
                "Number": "0086075512345678",
                "CallOutSkillGroupIds": [
                    1
                ]
            }
        ],
        "RequestId": "xx"
    }
}
```

