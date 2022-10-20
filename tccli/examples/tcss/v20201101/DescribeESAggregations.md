**Example 1: 获取ES字段聚合结果**



Input: 

```
tccli tcss DescribeESAggregations --cli-unfold-argument  \
    --Query {"index":["netflow"],"body":{"query":{"bool":{"filter":{"bool":{"filter":{"range":{"timestamp":{"gte":1597075200000,"lte":1597161599999}}},"must":[],"must_not":[],"should":[]}}}},"aggs":{"src_port":{"terms":{"field":"src_port","size":500,"order":{"_count":"desc"}}},"dst_port":{"terms":{"field":"dst_port","size":500,"order":{"_count":"desc"}}}}}}
```

Output: 
```
{
    "Response": {
        "Data": "{\"took\":114,\"total\":352317,\"aggs\":{\"dst_port\":{\"doc_count_error_upper_bound\":30,\"sum_other_doc_count\":116350,\"buckets\":[{\"key\":445,\"key_as_string\":null,\"KeyNumber\":0,\"doc_count\":53456},{\"key\":80,\"key_as_string\":null,\"KeyNumber\":0,\"doc_count\":33405},{\"key\":443,\"key_as_string\":null,\"KeyNumber\":0,\"doc_count\":17870}]},\"src_port\":{\"doc_count_error_upper_bound\":40,\"sum_other_doc_count\":233518,\"buckets\":[{\"key\":43957,\"key_as_string\":null,\"KeyNumber\":0,\"doc_count\":9878},{\"key\":40416,\"key_as_string\":null,\"KeyNumber\":0,\"doc_count\":4187},{\"key\":49892,\"key_as_string\":null,\"KeyNumber\":0,\"doc_count\":4100}]}},\"code\":0,\"message\":\"success\"}",
        "RequestId": "e4ee7f6c-a036-43e7-b98f-96f174827fea"
    }
}
```

