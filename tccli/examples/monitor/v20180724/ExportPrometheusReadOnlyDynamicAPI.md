**Example 1: 点查询(Instant query)**

```
Path: api/v1/query
Method: GET POST
Query参数: 
   1. query = <string> prometheus查询表达式
   2. time = <rfc3339 | unix_timestamp> 查询数据的时间
   3. timeout = <duration> 超时时间 (1m / 5s / ...)
响应体:
{
	"status": "success" | "error",
	"data": {
		"resultType": "matrix" | "vector" | "scalar" | "string",
		"result": <value>
	},
	
	// 错误时返回
	"errorType": "<string>",
	"error": "<string>",

	// warning 信息
	"warnings": ["<string>"]
}
```
查询结果result字段参考[prometheus点查询结果编码](https://prometheus.io/docs/prometheus/latest/querying/api/#expression-query-result-formats)

Input: 

```
tccli monitor ExportPrometheusReadOnlyDynamicAPI --cli-unfold-argument  \
    --InstanceId prom-xz223asd \
    --Method GET \
    --Path /api/v1/query?query=ALERTS{}&time=1700534157&timeout=30s
```

Output: 
```
{
    "Response": {
        "HTTP": {
            "StatusCode": 200,
            "ResponseBody": "{\"status\":\"success\",\"data\":{\"resultType\":\"vector\",\"result\":[{\"metric\":{\"__name__\":\"ALERTS\",\"_appid_\":\"1251763868\",\"_instanceid_\":\"prom-7031abs0\",\"_language_\":\"zh-CN\",\"_policyname_\":\"alertgroup-in-tke/alert-2\",\"_region_\":\"ap-chongqing\",\"_regionid_\":\"19\",\"_subaccountuin_\":\"4611686018429437801\",\"_uin_\":\"1500000688\",\"alertname\":\"alertgroup-in-tke/alert-2\",\"alertstate\":\"firing\",\"severity\":\"warning\",\"tcloud_region_id\":\"19\",\"tcloud_region_name\":\"ap-chongqing\"},\"value\":[1700534157,\"1\"]},{\"metric\":{\"__name__\":\"ALERTS\",\"_appid_\":\"1251763868\",\"_instanceid_\":\"prom-7031abs0\",\"_interval_\":\"5m\",\"_language_\":\"zh-CN\",\"_policyid_\":\"arule-2wou7mfi\",\"_policyname_\":\"test-monitor-alert\",\"_region_\":\"ap-chongqing\",\"_regionid_\":\"19\",\"_subaccountuin_\":\"100026263254\",\"_uin_\":\"1500000688\",\"alertname\":\"test-monitor-alert\",\"alertstate\":\"firing\",\"tcloud_region_id\":\"19\",\"tcloud_region_name\":\"ap-chongqing\"},\"value\":[1700534157,\"1\"]},{\"metric\":{\"__name__\":\"ALERTS\",\"_appid_\":\"1251763868\",\"_instanceid_\":\"prom-7031abs0\",\"_language_\":\"zh-CN\",\"_policyname_\":\"al-test-changed/aaaaa\",\"_region_\":\"ap-chongqing\",\"_regionid_\":\"19\",\"_subaccountuin_\":\"100026263254\",\"_uin_\":\"1500000688\",\"alertname\":\"al-test-changed/aaaaa\",\"alertstate\":\"firing\",\"tcloud_region_id\":\"19\",\"tcloud_region_name\":\"ap-chongqing\"},\"value\":[1700534157,\"1\"]},{\"metric\":{\"__name__\":\"ALERTS\",\"_appid_\":\"1251763868\",\"_instanceid_\":\"prom-7031abs0\",\"_language_\":\"zh-CN\",\"_policyname_\":\"alertgroup-in-tke/alert-1\",\"_region_\":\"ap-chongqing\",\"_regionid_\":\"19\",\"_subaccountuin_\":\"4611686018429437801\",\"_uin_\":\"1500000688\",\"alertname\":\"alertgroup-in-tke/alert-1\",\"alertstate\":\"firing\",\"severity\":\"warning\",\"tcloud_region_id\":\"19\",\"tcloud_region_name\":\"ap-chongqing\"},\"value\":[1700534157,\"1\"]}]}}"
        },
        "RequestId": "8-ztbsc3gc2-rw6lzn4gfg5kuz6khrxg"
    }
}
```

