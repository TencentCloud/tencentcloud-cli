**Example 1: 查询 AIGC API Token 列表。**



Input: 

```
tccli vod DescribeAigcApiTokens --cli-unfold-argument  \
    --SubAppId 251006666
```

Output: 
```
{
    "Response": {
        "RequestId": "12ae8d8e-dce3-4151-9d4b-5594145287e1",
        "ApiTokens": [
            "dqFQejeK2BMU8PRmc57gx9OSGKa72PwN",
            "8Tul4P4EiJKZ80AfF11HApbYSyK4uj1e"
        ]
    }
}
```

