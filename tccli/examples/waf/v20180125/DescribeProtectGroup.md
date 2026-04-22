**Example 1: 获取防护对象组详情**



Input: 

```
tccli waf DescribeProtectGroup --cli-unfold-argument  \
    --Filter.0.Name ID \
    --Filter.0.Values 11101 \
    --Filter.0.ExactMatch True
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "ID": 11101,
                "Name": "xxx",
                "Remark": "remark",
                "RuleNum": 12,
                "Domains": [
                    {
                        "Domain": "www.testwaf.com",
                        "Instances": [
                            {
                                "ID": "waf_int0dxss",
                                "Name": "waf_instance"
                            }
                        ]
                    }
                ]
            }
        ],
        "Total": 122,
        "RequestId": "xxxx"
    }
}
```

