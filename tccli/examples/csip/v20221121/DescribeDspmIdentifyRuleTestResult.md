**Example 1: DescribeDspmIdentifyRuleTestResult**



Input: 

```
tccli csip DescribeDspmIdentifyRuleTestResult --cli-unfold-argument  \
    --RuleType Structured \
    --RuleContent {"NodeType":"operator","OptType":"or","RuleInfos":[],"Nodes":[{"NodeType":"operator","OptType":"and","RuleInfos":[{"DataSourceType":"field_name","RuleMethod":"match","RuleType":"keyword","RuleContent":"email"}],"Nodes":[]}]} \
    --RuleId 5807 \
    --MemberId mem-12e1wq1e \
    --StructuredTestContent.0.Name field_name \
    --StructuredTestContent.0.Value email \
    --UnStructuredTestContent kyrie@tencent.com
```

Output: 
```
{
    "Response": {
        "IsMatch": true,
        "RequestId": "f78a4edb-b592-48f6-b2af-04ebfde252be"
    }
}
```

