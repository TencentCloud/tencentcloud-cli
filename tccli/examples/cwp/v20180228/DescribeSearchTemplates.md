**Example 1: 获取快速检索列表**



Input: 

```
tccli cwp DescribeSearchTemplates --cli-unfold-argument  \
    --Offset 0 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "TotalCount": 2,
        "List": [
            {
                "Id": 17,
                "Name": "kbtest",
                "LogType": "malware",
                "Condition": "src_ip 匹配字符: 193.27.228.98",
                "TimeRange": "2020-07-31 00:00:00 至 2020-07-31 23:59:59",
                "Query": "{\"index\":[\"malware\"],\"body\":{\"query\":{\"bool\":{\"filter\":{\"bool\":{\"filter\":{\"range\":{\"timestamp\":{\"gte\":1596124800000,\"lte\":1596211199999}}},\"must\":[{\"term\":{\"src_ip\":\"193.27.228.98\"}}],\"must_not\":[],\"should\":[]}}}},\"aggs\":{\"count_stats\":{\"date_histogram\":{\"field\":\"timestamp\",\"interval\":\"30m\",\"time_zone\":\"Asia/Shanghai\",\"min_doc_count\":1}}},\"highlight\":{\"fields\":{\"*\":{}}}},\"sort\":[{\"timestamp\":\"desc\"}]}",
                "Flag": "simple",
                "DisplayData": "[{\"id\":14401398135,\"patternsField\":\"src_ip\",\"selectedtype\":\"is\",\"selectedOptionsMap\":{\"is\":\"匹配字符\",\"like\":\"模糊匹配字符\",\"not\":\"不包含字符\",\"is_one_of\":\"匹配以下任意字符\",\"not_one_of\":\"不包含以下任意字符\"},\"selectedTypeList\":[\"is\",\"like\",\"not\",\"is_one_of\",\"not_one_of\"],\"third_cat\":\"input\",\"value\":\"193.27.228.98\"}]"
            },
            {
                "Id": 13,
                "Name": "test",
                "LogType": "malware",
                "Condition": "src_ip 匹配字符: 10.0.0.1",
                "TimeRange": "2020-06-13 00:00:00 至 2020-07-13 23:59:59",
                "Query": "{\"index\":[\"malware\"],\"body\":{\"query\":{\"bool\":{\"filter\":{\"bool\":{\"filter\":{\"range\":{\"timestamp\":{\"gte\":1591977600000,\"lte\":1594655999999}}},\"must\":[{\"term\":{\"src_ip\":\"10.0.0.1\"}}],\"must_not\":[],\"should\":[]}}}},\"aggs\":{\"count_stats\":{\"date_histogram\":{\"field\":\"timestamp\",\"interval\":\"12h\",\"time_zone\":\"Asia/Shanghai\",\"min_doc_count\":1}}},\"highlight\":{\"fields\":{\"*\":{}}}},\"sort\":[{\"timestamp\":\"desc\"}]}",
                "Flag": "simple",
                "DisplayData": "[{\"id\":449375484687,\"patternsField\":\"src_ip\",\"selectedtype\":\"is\",\"selectedOptionsMap\":{\"is\":\"匹配字符\",\"like\":\"模糊匹配字符\",\"not\":\"不包含字符\",\"is_one_of\":\"匹配以下任意字符\",\"not_one_of\":\"不包含以下任意字符\"},\"selectedTypeList\":[\"is\",\"like\",\"not\",\"is_one_of\",\"not_one_of\"],\"third_cat\":\"input\",\"value\":\"10.0.0.1\"}]"
            }
        ],
        "RequestId": "252ab6a8-3d45-414d-a31e-fb668e99864c"
    }
}
```

