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
tccli monitor ExportPrometheusReadOnlyDynamicAPI --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "8-ztbsc3gc2-rw6lzn4gfg5kuz6khrxg"
    }
}
```

