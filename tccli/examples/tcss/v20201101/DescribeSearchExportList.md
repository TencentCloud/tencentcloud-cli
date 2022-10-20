**Example 1: 导出ES查询文档列表**



Input: 

```
tccli tcss DescribeSearchExportList --cli-unfold-argument  \
    --Query {"index":["netflow"],"body":{"query":{"bool":{"filter":{"bool":{"filter":{"range":{"timestamp":{"gte":1597075200000,"lte":1597161599999}}},"must":[],"must_not":[],"should":[]}}}},"highlight":{"fields":{"*":{}}}},"sort":[{"timestamp":"desc"}]}
```

Output: 
```
{
    "Response": {
        "JobId": "1223",
        "RequestId": "e4ee7f6c-a036-43e7-b98f-96f174827fea"
    }
}
```

