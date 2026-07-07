**Example 1: 修改dspm数据识别数据项**



Input: 

```
tccli csip ModifyDspmIdentifyRule --cli-unfold-argument  \
    --Id 10357 \
    --Name 自定义手机号识别 \
    --MemberId mem-12e13wd1 \
    --Status 1 \
    --StructuredRule {"NodeType":"operator","OptType":"and","Nodes":[{"NodeType":"operator","OptType":"and","RuleInfos":[{"DataSourceType":"field_value","RuleMethod":"match","RuleType":"keyword","RuleContent":"phone","Parameters":{"IsIgnoreCase":"true"}}],"Nodes":[]}]} \
    --UnStructuredRule {"RegexRule":{"Operator":"or","Contents":[{"RuleContent":"(?<=\\D)(13[0-9]|14[014-9]|15[0-35-9]|16[2567]|17[0-8]|18[0-9]|19[0-35-9])\\d{8}(?=\\D)","IsIgnoreCase":true}]},"MaxMatchRule":{"Length":100}}
```

Output: 
```
{
    "Response": {
        "RequestId": "7cb25fcd-6d28-4514-8b30-2585163ab240"
    }
}
```

