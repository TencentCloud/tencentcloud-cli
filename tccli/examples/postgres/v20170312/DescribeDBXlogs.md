**Example 1: 获取实例postgres-apzvwncr的Xlog列表**

获取实例postgres-apzvwncr在2018-06-10 17:06:38至2018-06-11 17:06:38时间内的Xlog列表。

Input: 

```
tccli postgres DescribeDBXlogs --cli-unfold-argument  \
    --EndTime 2018-06-11 17:06:38 \
    --DBInstanceId postgres-apzvwncr \
    --StartTime 2018-06-10 17:06:38
```

Output: 
```
{
    "Response": {
        "TotalCount": 6,
        "XlogList": [
            {
                "StartTime": "2018-06-22 01:56:46",
                "InternalAddr": "http://172.16.16.30:8366/download/20180622015646_20180622015653.tar.gz?giz7Z4LlMjal0S0oJY6+5JbQ1MfhjybTALKlriBmLUrmJMxzi1C3EagZ/IhOQeSGyXm+Qr3D3I2GL1G4RV69vLVylUaeIJ+zH+CEG5Ast0GoDmpzjJ5Jaw==",
                "EndTime": "2018-06-22 01:56:53",
                "ExternalAddr": "https://gz-dl-postgres.cloud.tencent.com/download/20180622015646_20180622015653.tar.gz?giz7Z4LlMjal0S0oJY6+5JbQ1MfhjybTALKlriBmLUrmJMxzi1C3EagZ/IhOQeSGyXm+Qr3D3I2GL1G4RV69vLVylUaeIJ+zH+CEG5Ast0GoDmpzjJ5Jaw==",
                "Id": 450,
                "Size": 247967
            },
            {
                "StartTime": "2018-06-22 01:56:17",
                "InternalAddr": "http://172.16.16.30:8366/download/20180622015617_20180622015645.tar.gz?giz7Z4LlMjal0S0oJY6+5JbQ1MfhjybTALKlriBmLUrmJMxzi1C3Eamxg5sq4mNUSXLgasiI8P5xiJVUBOrLUPKLYacTxFWP8y56/f36byxdYH5+PGMzOA==",
                "EndTime": "2018-06-22 01:56:45",
                "ExternalAddr": "https://gz-dl-postgres.cloud.tencent.com/download/20180622015617_20180622015645.tar.gz?giz7Z4LlMjal0S0oJY6+5JbQ1MfhjybTALKlriBmLUrmJMxzi1C3Eamxg5sq4mNUSXLgasiI8P5xiJVUBOrLUPKLYacTxFWP8y56/f36byxdYH5+PGMzOA==",
                "Id": 450,
                "Size": 899618
            },
            {
                "StartTime": "2018-06-22 01:56:10",
                "InternalAddr": "http://172.16.16.30:8366/download/20180622015610_20180622015610.tar.gz?giz7Z4LlMjal0S0oJY6+5JbQ1MfhjybTALKlriBmLUrmJMxzi1C3EWUN67hkmzzI32w2wS4KNi5jqNoaHxSJ59WJ9lrYebaz9SZgdOXyUBxlFmOGNchE3Q==",
                "EndTime": "2018-06-22 01:56:10",
                "ExternalAddr": "https://gz-dl-postgres.cloud.tencent.com/download/20180622015610_20180622015610.tar.gz?giz7Z4LlMjal0S0oJY6+5JbQ1MfhjybTALKlriBmLUrmJMxzi1C3EWUN67hkmzzI32w2wS4KNi5jqNoaHxSJ59WJ9lrYebaz9SZgdOXyUBxlFmOGNchE3Q==",
                "Id": 450,
                "Size": 41749
            },
            {
                "StartTime": "2018-06-21 01:55:49",
                "InternalAddr": "http://172.16.16.30:8366/download/20180621015549_20180621015557.tar.gz?giz7Z4LlMjal0S0oJY6+5JbQ1MfhjybTGXfsNyKOxst2LTlcd0/LLPjSmz1BP/DJbQOeznMtdJsr77l4alcITO6f+jyIZ0upCYIFZhCIO2iJSzDXktIsGg==",
                "EndTime": "2018-06-21 01:55:57",
                "ExternalAddr": "https://gz-dl-postgres.cloud.tencent.com/download/20180621015549_20180621015557.tar.gz?giz7Z4LlMjal0S0oJY6+5JbQ1MfhjybTGXfsNyKOxst2LTlcd0/LLPjSmz1BP/DJbQOeznMtdJsr77l4alcITO6f+jyIZ0upCYIFZhCIO2iJSzDXktIsGg==",
                "Id": 450,
                "Size": 247941
            },
            {
                "StartTime": "2018-06-21 01:55:20",
                "InternalAddr": "http://172.16.16.30:8366/download/20180621015520_20180621015548.tar.gz?giz7Z4LlMjal0S0oJY6+5JbQ1MfhjybTGXfsNyKOxst2LTlcd0/LLNhfLPY0y78Bi9G0LEDTC70hI3QKhTP7jWZT/+e51oyIRW6hm8MoEKQ2DyBqjqvtaQ==",
                "EndTime": "2018-06-21 01:55:48",
                "ExternalAddr": "https://gz-dl-postgres.cloud.tencent.com/download/20180621015520_20180621015548.tar.gz?giz7Z4LlMjal0S0oJY6+5JbQ1MfhjybTGXfsNyKOxst2LTlcd0/LLNhfLPY0y78Bi9G0LEDTC70hI3QKhTP7jWZT/+e51oyIRW6hm8MoEKQ2DyBqjqvtaQ==",
                "Id": 450,
                "Size": 899646
            },
            {
                "StartTime": "2018-06-21 01:55:13",
                "InternalAddr": "http://172.16.16.30:8366/download/20180621015513_20180621015513.tar.gz?giz7Z4LlMjal0S0oJY6+5JbQ1MfhjybTGXfsNyKOxst2LTlcd0/LLKcr1q+wVdmFDDcdUtRcVsPlqfMXXg63tRWRtX/jFz6/MNbKg3r+EDkD5NdLA4nWhw==",
                "EndTime": "2018-06-21 01:55:13",
                "ExternalAddr": "https://gz-dl-postgres.cloud.tencent.com/download/20180621015513_20180621015513.tar.gz?giz7Z4LlMjal0S0oJY6+5JbQ1MfhjybTGXfsNyKOxst2LTlcd0/LLKcr1q+wVdmFDDcdUtRcVsPlqfMXXg63tRWRtX/jFz6/MNbKg3r+EDkD5NdLA4nWhw==",
                "Id": 450,
                "Size": 41744
            }
        ],
        "RequestId": "08fdf411-5d39-44f2-8e1d-a58ee60b237d"
    }
}
```

