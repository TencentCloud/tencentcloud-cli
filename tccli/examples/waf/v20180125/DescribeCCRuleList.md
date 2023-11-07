**Example 1: 根据URL查询API规则**



Input: 

```
tccli waf DescribeCCRuleList --cli-unfold-argument  \
    --Domain www.testwaf.com \
    --Limit 1 \
    --Filters.0.Values clb saas \
    --Filters.0.Name InstanceType \
    --Filters.0.ExactMatch True \
    --Offset 1 \
    --By ts_version
```

Output: 
```
{
    "Response": {
        "RequestId": "1cc54bf4-cfeb-40cc-a823-035e52106df9"
    }
}
```

**Example 2: test1**



Input: 

```
tccli waf DescribeCCRuleList --cli-unfold-argument  \
    --By ts_version \
    --Domain hzh.qcloud.com \
    --Limit 10 \
    --Order asc \
    --Offset 10000002
```

Output: 
```
{
    "Response": {
        "RequestId": "41b55f8b-1ed1-484c-aab7-c14c0889f78b"
    }
}
```

