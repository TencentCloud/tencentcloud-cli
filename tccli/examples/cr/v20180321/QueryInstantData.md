**Example 1: 查询入催外呼数据**



Input: 

```
tccli cr QueryInstantData --cli-unfold-argument  \
    --Module Data \
    --Operation Query \
    --Offset 0 \
    --Limit 10 \
    --InstanceId ins-a1b2c3 \
    --Data '"{\"StartBizDate\":\"2019-03-03\", \"EndBizDate\":\"2019-03-13\"}"'
```

Output: 
```
{
    "Response": {
        "Data": "[{\"AccountNum\":\"QK071200000001\",\"BizDate\":\"2019-03-05\",\"CallStartTime\":\"2019-03-05 13:00:00\",\"CallerPhone\":\"0105555333\",\"Direction\":\"O\",\"Duration\":15,\"ProductId\":null,\"RecordCosUrl\":\"http://cr.cosgz.myqcloud.com/cnc/cr-record-ab-f30\"}]",
        "RequestId": "",
        "TotalCount": 1
    }
}
```

