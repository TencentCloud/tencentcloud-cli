**Example 1: 创建日志集。**

创建日志集。

Input: 

```
tccli clb CreateClsLogSet --cli-unfold-argument  \
    --LogsetName clb_logset \
    --Period 7
```

Output: 
```
{
    "Response": {
        "LogsetId": "578dd0ad-2e7c-488b-b5fe-0b23da3537eb",
        "RequestId": "8b038842-70b2-411b-a1a2-c7fcde195d2c"
    }
}
```

