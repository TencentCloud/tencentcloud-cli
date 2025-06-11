**Example 1: 获取云梯子账号有权限的标签列表**



Input: 

```
tccli cloudrc ListYuntiTagAuthorizations --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "List": [
            {
                "Key": "负责人",
                "Value": "brucelee"
            },
            {
                "Key": "运营产品",
                "Value": "腾讯云计费产品其它_1649"
            },
            {
                "Key": "备份负责人",
                "Value": "brucelee"
            }
        ],
        "RequestId": "d1cb6f59-d210-4e9a-a0cd-688cb4364f17"
    }
}
```

