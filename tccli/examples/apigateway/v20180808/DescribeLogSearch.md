**Example 1: Filters参数示例**

LogQuerys 表示日志检索条件，
其中: LogQuerys.0.Name=api_id&LogQuerys.0.Operator==&LogQuerys.0.Value=api-55rj9ide
表示检索api_id=api-55rj9ide的日志

Input: 

```
tccli apigateway DescribeLogSearch --cli-unfold-argument  \
    --StartTime '2020-05-28 22:00:00' \
    --EndTime '2020-05-28 23:00:00' \
    --ServiceId service-8xipv0ua \
    --LogQuerys.0.Name api_id \
    --LogQuerys.0.Operator  \
    --LogQuerys.0.Value api-55rj9ide
```

Output: 
```
{
    "Response": {
        "ConText": "Y29udGV4dC0xOTE1NTdiOS04YjVhLTRkZWQtODA5YS0zOTg2MmY0ZjdkN2MxNTkwNjc3NzU5NTcy",
        "TotalCount": 20,
        "LogSet": [
            "[1300127097][release][service-8xipv0ua][service-8xipv0ua-1300127097.gz.apigw.tencentcs.com][api-55rj9ide][/][http][rsp_st:200][ups_st:-][cip:119.123.71.59][uip:-][vip:193.112.148.212][rsp_len:328][req_len:114][req_t:0.000][ups_rsp_t:-][ups_conn_t:-][ups_head_t:-][err_msg:-][tcp_rtt:12500][20260][28/May/2020:22:42:42 +0800][req_id:a26f8eaf6ef7e4ef466a25036332139a]",
            "[1300127097][release][service-8xipv0ua][service-8xipv0ua-1300127097.gz.apigw.tencentcs.com][api-55rj9ide][/][http][rsp_st:200][ups_st:-][cip:119.123.71.59][uip:-][vip:193.112.148.212][rsp_len:328][req_len:114][req_t:0.000][ups_rsp_t:-][ups_conn_t:-][ups_head_t:-][err_msg:-][tcp_rtt:13500][20247][28/May/2020:22:42:41 +0800][req_id:53500963839556bc40ae185c2a135353]",
            "[1300127097][release][service-8xipv0ua][service-8xipv0ua-1300127097.gz.apigw.tencentcs.com][api-55rj9ide][/][http][rsp_st:200][ups_st:-][cip:119.123.71.59][uip:-][vip:193.112.148.212][rsp_len:328][req_len:114][req_t:0.000][ups_rsp_t:-][ups_conn_t:-][ups_head_t:-][err_msg:-][tcp_rtt:12500][20244][28/May/2020:22:42:41 +0800][req_id:e4a934687379333230168e4674655b00]",
            "[1300127097][release][service-8xipv0ua][service-8xipv0ua-1300127097.gz.apigw.tencentcs.com][api-55rj9ide][/][http][rsp_st:200][ups_st:-][cip:119.123.71.59][uip:-][vip:193.112.148.212][rsp_len:328][req_len:114][req_t:0.000][ups_rsp_t:-][ups_conn_t:-][ups_head_t:-][err_msg:-][tcp_rtt:12500][20261][28/May/2020:22:42:41 +0800][req_id:74ddc940596054cd16fc7b2ccfa6b36d]",
            "[1300127097][release][service-8xipv0ua][service-8xipv0ua-1300127097.gz.apigw.tencentcs.com][api-55rj9ide][/][http][rsp_st:200][ups_st:-][cip:119.123.71.59][uip:-][vip:193.112.148.212][rsp_len:328][req_len:114][req_t:0.000][ups_rsp_t:-][ups_conn_t:-][ups_head_t:-][err_msg:-][tcp_rtt:14000][20240][28/May/2020:22:42:40 +0800][req_id:ad1f06dd126d10930dbed41c2dbcd90a]",
            "[1300127097][release][service-8xipv0ua][service-8xipv0ua-1300127097.gz.apigw.tencentcs.com][api-55rj9ide][/][http][rsp_st:200][ups_st:-][cip:119.123.71.59][uip:-][vip:193.112.148.212][rsp_len:328][req_len:114][req_t:0.000][ups_rsp_t:-][ups_conn_t:-][ups_head_t:-][err_msg:-][tcp_rtt:14500][20253][28/May/2020:22:42:40 +0800][req_id:56865fe7631a4ca9efaaeeeebe739707]",
            "[1300127097][release][service-8xipv0ua][service-8xipv0ua-1300127097.gz.apigw.tencentcs.com][api-55rj9ide][/][http][rsp_st:200][ups_st:-][cip:119.123.71.59][uip:-][vip:193.112.148.212][rsp_len:328][req_len:114][req_t:0.000][ups_rsp_t:-][ups_conn_t:-][ups_head_t:-][err_msg:-][tcp_rtt:14000][20249][28/May/2020:22:42:39 +0800][req_id:51a305fc4f84248695b0313f58002e54]",
            "[1300127097][release][service-8xipv0ua][service-8xipv0ua-1300127097.gz.apigw.tencentcs.com][api-55rj9ide][/][http][rsp_st:200][ups_st:-][cip:119.123.71.59][uip:-][vip:193.112.148.212][rsp_len:328][req_len:114][req_t:0.000][ups_rsp_t:-][ups_conn_t:-][ups_head_t:-][err_msg:-][tcp_rtt:15500][20273][28/May/2020:22:42:39 +0800][req_id:81cc0eb9d1cabe580c0f91e4cd514b6a]",
            "[1300127097][release][service-8xipv0ua][service-8xipv0ua-1300127097.gz.apigw.tencentcs.com][api-55rj9ide][/][http][rsp_st:200][ups_st:-][cip:119.123.71.59][uip:-][vip:193.112.148.212][rsp_len:328][req_len:114][req_t:0.000][ups_rsp_t:-][ups_conn_t:-][ups_head_t:-][err_msg:-][tcp_rtt:16000][20254][28/May/2020:22:42:38 +0800][req_id:138467bbff388882dadf7d101ff321e0]",
            "[1300127097][release][service-8xipv0ua][service-8xipv0ua-1300127097.gz.apigw.tencentcs.com][api-55rj9ide][/][http][rsp_st:200][ups_st:-][cip:119.123.71.59][uip:-][vip:193.112.148.212][rsp_len:328][req_len:114][req_t:0.000][ups_rsp_t:-][ups_conn_t:-][ups_head_t:-][err_msg:-][tcp_rtt:14500][20236][28/May/2020:22:42:38 +0800][req_id:bd80236f63a0cc276b3e37596aadd41b]",
            "[1300127097][release][service-8xipv0ua][service-8xipv0ua-1300127097.gz.apigw.tencentcs.com][api-55rj9ide][/][http][rsp_st:200][ups_st:-][cip:119.123.71.59][uip:-][vip:193.112.148.212][rsp_len:328][req_len:114][req_t:0.000][ups_rsp_t:-][ups_conn_t:-][ups_head_t:-][err_msg:-][tcp_rtt:11500][20259][28/May/2020:22:42:37 +0800][req_id:a9f65829cf6e6b89f1ac1667eb1f7917]",
            "[1300127097][release][service-8xipv0ua][service-8xipv0ua-1300127097.gz.apigw.tencentcs.com][api-55rj9ide][/][http][rsp_st:200][ups_st:-][cip:119.123.71.59][uip:-][vip:193.112.148.212][rsp_len:328][req_len:114][req_t:0.000][ups_rsp_t:-][ups_conn_t:-][ups_head_t:-][err_msg:-][tcp_rtt:11500][20246][28/May/2020:22:42:37 +0800][req_id:946d51c39f23bdc99f1949420aab32cb]",
            "[1300127097][release][service-8xipv0ua][service-8xipv0ua-1300127097.gz.apigw.tencentcs.com][api-55rj9ide][/][http][rsp_st:200][ups_st:-][cip:119.123.71.59][uip:-][vip:193.112.148.212][rsp_len:328][req_len:114][req_t:0.000][ups_rsp_t:-][ups_conn_t:-][ups_head_t:-][err_msg:-][tcp_rtt:11500][20252][28/May/2020:22:42:36 +0800][req_id:e762ac1b039098de1d140b4369c3e478]",
            "[1300127097][release][service-8xipv0ua][service-8xipv0ua-1300127097.gz.apigw.tencentcs.com][api-55rj9ide][/][http][rsp_st:200][ups_st:-][cip:119.123.71.59][uip:-][vip:193.112.148.212][rsp_len:328][req_len:114][req_t:0.000][ups_rsp_t:-][ups_conn_t:-][ups_head_t:-][err_msg:-][tcp_rtt:11500][20235][28/May/2020:22:42:36 +0800][req_id:0b353eac83a78dbdaa6366f5ec5dedfc]",
            "[1300127097][release][service-8xipv0ua][service-8xipv0ua-1300127097.gz.apigw.tencentcs.com][api-55rj9ide][/][http][rsp_st:200][ups_st:-][cip:119.123.71.59][uip:-][vip:193.112.148.212][rsp_len:328][req_len:114][req_t:0.000][ups_rsp_t:-][ups_conn_t:-][ups_head_t:-][err_msg:-][tcp_rtt:12500][20247][28/May/2020:22:42:35 +0800][req_id:55371f19fb83913ff86755c2ae52362c]",
            "[1300127097][release][service-8xipv0ua][service-8xipv0ua-1300127097.gz.apigw.tencentcs.com][api-55rj9ide][/][http][rsp_st:200][ups_st:-][cip:119.123.71.59][uip:-][vip:193.112.148.212][rsp_len:328][req_len:114][req_t:0.000][ups_rsp_t:-][ups_conn_t:-][ups_head_t:-][err_msg:-][tcp_rtt:12000][20268][28/May/2020:22:42:35 +0800][req_id:32ab8e63e7dfaa8b553ba58085fd754c]",
            "[1300127097][release][service-8xipv0ua][service-8xipv0ua-1300127097.gz.apigw.tencentcs.com][api-55rj9ide][/][http][rsp_st:200][ups_st:-][cip:119.123.71.59][uip:-][vip:193.112.148.212][rsp_len:328][req_len:114][req_t:0.000][ups_rsp_t:-][ups_conn_t:-][ups_head_t:-][err_msg:-][tcp_rtt:12500][20232][28/May/2020:22:42:34 +0800][req_id:21c6c7c1e21bc7e39c290bf3d56bd3ba]",
            "[1300127097][release][service-8xipv0ua][service-8xipv0ua-1300127097.gz.apigw.tencentcs.com][api-55rj9ide][/][http][rsp_st:200][ups_st:-][cip:119.123.71.59][uip:-][vip:193.112.148.212][rsp_len:328][req_len:114][req_t:0.000][ups_rsp_t:-][ups_conn_t:-][ups_head_t:-][err_msg:-][tcp_rtt:12000][20263][28/May/2020:22:42:33 +0800][req_id:3970867bbb023265a03b86d49ef52b59]",
            "[1300127097][release][service-8xipv0ua][service-8xipv0ua-1300127097.gz.apigw.tencentcs.com][api-55rj9ide][/][http][rsp_st:200][ups_st:-][cip:119.123.71.59][uip:-][vip:193.112.148.212][rsp_len:328][req_len:114][req_t:0.000][ups_rsp_t:-][ups_conn_t:-][ups_head_t:-][err_msg:-][tcp_rtt:12000][20255][28/May/2020:22:42:33 +0800][req_id:caaa1b83b0bcd7a5b1325281769b9364]",
            "[1300127097][release][service-8xipv0ua][service-8xipv0ua-1300127097.gz.apigw.tencentcs.com][api-55rj9ide][/][http][rsp_st:200][ups_st:-][cip:119.123.71.59][uip:-][vip:193.112.148.212][rsp_len:328][req_len:114][req_t:0.000][ups_rsp_t:-][ups_conn_t:-][ups_head_t:-][err_msg:-][tcp_rtt:8500][20246][28/May/2020:22:42:32 +0800][req_id:64866292cce1f59504e4ae30796d3731]"
        ],
        "RequestId": "239c9af4-2e79-4252-b5e5-c7a4c0c7f743"
    }
}
```

**Example 2: 请求失败**

下面的示例提示参数错误

Input: 

```
tccli apigateway DescribeLogSearch --cli-unfold-argument  \
    --StartTime '2019-10-10 00:00:00' \
    --EndTime '2019-10-10 23:59:59' \
    --ServiceId service-8xipv0ua \
    --Limit 101
```

Output: 
```
{
    "Response": {
        "RequestId": "5a8b1de4-04f5-48eb-9be6-93491ebee6e1"
    }
}
```

