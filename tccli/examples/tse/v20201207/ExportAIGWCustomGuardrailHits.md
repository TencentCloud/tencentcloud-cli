**Example 1: 导出 JSON 审核记录**

将 Content 做 Base64 解码即可得到 JSON 数组，不要把 Content 当 URL 访问。 这是说明性示例，未执行真实资源操作；响应字段以目标环境实际部署版本为准。

Input: 

```
tccli tse ExportAIGWCustomGuardrailHits --cli-unfold-argument  \
    --GatewayId gateway-12345678 \
    --StartTime 1788832800 \
    --EndTime 1788836400 \
    --Filters.0.Name PolicyId \
    --Filters.0.Values 11111111-1111-4111-8111-111111111111 \
    --Filters.1.Name Direction \
    --Filters.1.Values response \
    --Format json
```

Output: 
```
{
    "Response": {
        "Result": {
            "Format": "json",
            "RowCount": 1,
            "Truncated": false,
            "Content": "W3siUmVxdWVzdElkIjoiNzc3Nzc3NzctNzc3Ny00Nzc3LTg3NzctNzc3Nzc3Nzc3Nzc3IiwiVGltZXN0YW1wIjoxNzg4ODMzMTAwMTIzLCJHYXRld2F5SWQiOiJnYXRld2F5LTEyMzQ1Njc4IiwiUG9saWN5SWQiOiIxMTExMTExMS0xMTExLTQxMTEtODExMS0xMTExMTExMTExMTEiLCJQb2xpY3lOYW1lIjoibWNwLWN1c3RvbS1hdWRpdCIsIlJlc291cmNlVHlwZSI6Im1jcF9zZXJ2ZXIiLCJSZXNvdXJjZUlkIjoiMjIyMjIyMjItMjIyMi00MjIyLTgyMjItMjIyMjIyMjIyMjIyIiwiUm91dGVJZCI6IjQ0NDQ0NDQ0LTQ0NDQtNDQ0NC04NDQ0LTQ0NDQ0NDQ0NDQ0NCIsIlByb3RvY29sIjoibWNwLXN0cmVhbWFibGUtaHR0cCIsIkRpcmVjdGlvbiI6InJlc3BvbnNlIiwiU3RyZWFtaW5nIjp0cnVlLCJGaW5hbCI6ZmFsc2UsIkRlY2lzaW9uIjoiYmxvY2siLCJDb25maWd1cmVkQWN0aW9uIjoiYmxvY2siLCJFZmZlY3RpdmVBY3Rpb24iOiJibG9jayIsIlJld3JpdHRlbiI6ZmFsc2UsIkJsb2NrZWQiOnRydWUsIkRvd25ncmFkZWQiOmZhbHNlLCJQcm92aWRlclN0YXR1c0NvZGUiOjIwMCwiTGF0ZW5jeU1zIjo1Mi4zfV0="
        },
        "RequestId": "77777777-7777-4777-8777-777777777777"
    }
}
```

