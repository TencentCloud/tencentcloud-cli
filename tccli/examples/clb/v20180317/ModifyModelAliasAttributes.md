**Example 1: 修改输入输出系数**



Input: 

```
tccli clb ModifyModelAliasAttributes --cli-unfold-argument  \
    --Coefficient.InputCoefficient 123 \
    --Coefficient.InputCachedCoefficient 3 \
    --Coefficient.OutputCoefficient 321 \
    --ModelAliasNames gpt-4o
```

Output: 
```
{
    "Response": {
        "RequestId": "71c612f8-b634-4a3b-b9f8-dcb79e5f36ca"
    }
}
```

