**Example 1: 添加检索模板**



Input: 

```
tccli tcss CreateSearchTemplate --cli-unfold-argument  \
    --SearchTemplate.Id 1 \
    --SearchTemplate.Name test1 \
    --SearchTemplate.DisplayData [{"id":449375484687,"patternsField":"src_ip","selectedtype":"is","selectedOptionsMap":{"is":"匹配字符","like":"模糊匹配字符","not":"不包含字符","is_one_of":"匹配以下任意字符","not_one_of":"不包含以下任意字符"},"selectedTypeList":["is","like","not","is_one_of","not_one_of"],"third_cat":"input","value":"10.0.0.1"}] \
    --SearchTemplate.TimeRange 2020-06-1300:00:00至2020-07-1323:59:59 \
    --SearchTemplate.LogType malware \
    --SearchTemplate.Flag simple \
    --SearchTemplate.Query {"index":["malware"],"body":{"query":{"bool":{"filter":{"bool":{"filter":{"range":{"timestamp":{"gte":1591977600000,"lte":1594655999999}}},"must":[{"term":{"src_ip":"10.0.0.1"}}],"must_not":[],"should":[]}}}},"aggs":{"count_stats":{"date_histogram":{"field":"timestamp","interval":"12h","time_zone":"Asia/Shanghai","min_doc_count":1}}},"highlight":{"fields":{"*":{}}}},"sort":[{"timestamp":"desc"}]} \
    --SearchTemplate.Condition src_ip匹配字符:10.0.0.1
```

Output: 
```
{
    "Response": {
        "RequestId": "49082d4a-71b4-4e32-9ca1-b33872a4a63a"
    }
}
```

