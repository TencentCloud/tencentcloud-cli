**Example 1: 获取记录负载均衡信息**

 

Input: 

```
tccli dnspod DescribeRecordCountByRoll --cli-unfold-argument  \
    --Domain dnspod.site \
    --SubDomain www
```

Output: 
```
{
    "Response": {
        "RequestId": "ab4f1426-ea15-42ea-8183-dc1b44151166",
        "NowRoll": 2,
        "MaxRoll": 10,
        "GradeTitle": "专业版"
    }
}
```

