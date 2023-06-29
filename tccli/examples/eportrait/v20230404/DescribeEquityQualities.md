**Example 1: 查询指定企业的股权出质列表**

查询指定企业的股权出质列表

Input: 

```
tccli eportrait DescribeEquityQualities --cli-unfold-argument  \
    --Offset 0 \
    --Limit 45 \
    --Eid 0005c101a89284506b72095dba4465cf
```

Output: 
```
{
    "Response": {
        "TotalCount": 60,
        "RequestId": "727430cb-c15a-42ff-bb83-f0ef7500a4c5",
        "Data": [
            {
                "Eid": "0005c101a89284506b72095dba4465cf",
                "Number": "320684000343",
                "Pledgor": "袁备",
                "Pawnee": "先锋基金管理有限公司",
                "PledgorAmount": "43.8785",
                "Date": "2021-11-15",
                "Status": "有效"
            },
            {
                "Eid": "0005c101a89284506b72095dba4465cf",
                "Number": "320684000293",
                "Pledgor": "卫波",
                "Pawnee": "上海骁励企业管理合伙企业（有限合伙）",
                "PledgorAmount": "86.23",
                "Date": "2021-01-18",
                "Status": "有效"
            },
            {
                "Eid": "0005c101a89284506b72095dba4465cf",
                "Number": "320684000374",
                "Pledgor": "袁备",
                "Pawnee": "贵州大数据资本服务中心有限公司",
                "PledgorAmount": "4.7552",
                "Date": "2021-12-30",
                "Status": "有效"
            },
            {
                "Eid": "0005c101a89284506b72095dba4465cf",
                "Number": "320684000372",
                "Pledgor": "张福斌",
                "Pawnee": "贵州大数据资本服务中心有限公司",
                "PledgorAmount": "5.3631",
                "Date": "2021-12-30",
                "Status": "有效"
            },
            {
                "Eid": "0005c101a89284506b72095dba4465cf",
                "Number": "320684000198",
                "Pledgor": "黄裕辉",
                "Pawnee": "陆家嘴国际信托有限公司",
                "PledgorAmount": "2263.4414",
                "Date": "2017-12-27",
                "Status": "无效"
            },
            {
                "Eid": "0005c101a89284506b72095dba4465cf",
                "Number": "320684000360",
                "Pledgor": "周炳高",
                "Pawnee": "中天国富证券有限公司",
                "PledgorAmount": "164.4931",
                "Date": "2021-12-30",
                "Status": "有效"
            },
            {
                "Eid": "0005c101a89284506b72095dba4465cf",
                "Number": "320684000368",
                "Pledgor": "周炳高",
                "Pawnee": "贵州大数据资本服务中心有限公司",
                "PledgorAmount": "42.9047",
                "Date": "2021-12-30",
                "Status": "有效"
            },
            {
                "Eid": "0005c101a89284506b72095dba4465cf",
                "Number": "320684000299",
                "Pledgor": "黄裕辉",
                "Pawnee": "中国东方资产管理（国际）控股有限公司",
                "PledgorAmount": "3176.74",
                "Date": "2021-02-25",
                "Status": "有效"
            },
            {
                "Eid": "0005c101a89284506b72095dba4465cf",
                "Number": "320684000297",
                "Pledgor": "王卫冲",
                "Pawnee": "上海骁励企业管理合伙企业（有限合伙）",
                "PledgorAmount": "263.22",
                "Date": "2021-01-18",
                "Status": "有效"
            },
            {
                "Eid": "0005c101a89284506b72095dba4465cf",
                "Number": "320684000366",
                "Pledgor": "袁备",
                "Pawnee": "中天国富证券有限公司",
                "PledgorAmount": "18.2313",
                "Date": "2021-12-30",
                "Status": "有效"
            },
            {
                "Eid": "0005c101a89284506b72095dba4465cf",
                "Number": "320684000369",
                "Pledgor": "施晖",
                "Pawnee": "贵州大数据资本服务中心有限公司",
                "PledgorAmount": "39.955",
                "Date": "2021-12-30",
                "Status": "有效"
            },
            {
                "Eid": "0005c101a89284506b72095dba4465cf",
                "Number": "320684000364",
                "Pledgor": "张福斌",
                "Pawnee": "中天国富证券有限公司",
                "PledgorAmount": "20.5616",
                "Date": "2021-12-30",
                "Status": "有效"
            },
            {
                "Eid": "0005c101a89284506b72095dba4465cf",
                "Number": "320684000362",
                "Pledgor": "卫波",
                "Pawnee": "中天国富证券有限公司",
                "PledgorAmount": "20.5616",
                "Date": "2021-12-30",
                "Status": "有效"
            },
            {
                "Eid": "0005c101a89284506b72095dba4465cf",
                "Number": "320684000370",
                "Pledgor": "卫波",
                "Pawnee": "贵州大数据资本服务中心有限公司",
                "PledgorAmount": "5.3631",
                "Date": "2021-12-30",
                "Status": "有效"
            },
            {
                "Eid": "0005c101a89284506b72095dba4465cf",
                "Number": "320684000265",
                "Pledgor": "徐忠",
                "Pawnee": "招商银行股份有限公司南通分行",
                "PledgorAmount": "600.0",
                "Date": "2020-04-22",
                "Status": "无效"
            },
            {
                "Eid": "0005c101a89284506b72095dba4465cf",
                "Number": "320684000340",
                "Pledgor": "卫波",
                "Pawnee": "恒大人寿保险有限公司",
                "PledgorAmount": "86.9061",
                "Date": "2021-11-03",
                "Status": "有效"
            },
            {
                "Eid": "0005c101a89284506b72095dba4465cf",
                "Number": "320684000341",
                "Pledgor": "袁备",
                "Pawnee": "恒大人寿保险有限公司",
                "PledgorAmount": "33.1781",
                "Date": "2021-11-03",
                "Status": "有效"
            },
            {
                "Eid": "0005c101a89284506b72095dba4465cf",
                "Number": "320684000339",
                "Pledgor": "王卫冲",
                "Pawnee": "恒大人寿保险有限公司",
                "PledgorAmount": "5.9935",
                "Date": "2021-11-03",
                "Status": "有效"
            },
            {
                "Eid": "0005c101a89284506b72095dba4465cf",
                "Number": "320684000302",
                "Pledgor": "张福斌",
                "Pawnee": "Power Rider Enterprises Corp.",
                "PledgorAmount": "263.22",
                "Date": "2021-02-25",
                "Status": "有效"
            },
            {
                "Eid": "0005c101a89284506b72095dba4465cf",
                "Number": "320684000342",
                "Pledgor": "施晖",
                "Pawnee": "恒大人寿保险有限公司",
                "PledgorAmount": "238.8817",
                "Date": "2021-11-03",
                "Status": "有效"
            },
            {
                "Eid": "0005c101a89284506b72095dba4465cf",
                "Number": "320684000303",
                "Pledgor": "施晖",
                "Pawnee": "Power Rider Enterprises Corp.",
                "PledgorAmount": "140.68",
                "Date": "2021-02-25",
                "Status": "有效"
            },
            {
                "Eid": "0005c101a89284506b72095dba4465cf",
                "Number": "320684000365",
                "Pledgor": "徐挺",
                "Pawnee": "中天国富证券有限公司",
                "PledgorAmount": "20.5616",
                "Date": "2021-12-30",
                "Status": "有效"
            },
            {
                "Eid": "0005c101a89284506b72095dba4465cf",
                "Number": "320684000193",
                "Pledgor": "李华平",
                "Pawnee": "招商银行股份有限公司南通分行",
                "PledgorAmount": "700.0",
                "Date": "2017-09-29",
                "Status": "无效"
            },
            {
                "Eid": "0005c101a89284506b72095dba4465cf",
                "Number": "320684000295",
                "Pledgor": "施晖",
                "Pawnee": "上海骁励企业管理合伙企业（有限合伙）",
                "PledgorAmount": "1815.28",
                "Date": "2021-01-18",
                "Status": "有效"
            },
            {
                "Eid": "0005c101a89284506b72095dba4465cf",
                "Number": "320684000292",
                "Pledgor": "卫波",
                "Pawnee": "上海骁励企业管理合伙企业（有限合伙）",
                "PledgorAmount": "167.91",
                "Date": "2021-01-18",
                "Status": "有效"
            },
            {
                "Eid": "0005c101a89284506b72095dba4465cf",
                "Number": "320684000214",
                "Pledgor": "卫波",
                "Pawnee": "上实商业保理有限公司",
                "PledgorAmount": "200.0",
                "Date": "2018-11-26",
                "Status": "无效"
            },
            {
                "Eid": "0005c101a89284506b72095dba4465cf",
                "Number": "320684000117",
                "Pledgor": "王卫冲",
                "Pawnee": "上海建银国际投资咨询有限公司",
                "PledgorAmount": "245.0",
                "Date": "2016-07-11",
                "Status": "无效"
            },
            {
                "Eid": "0005c101a89284506b72095dba4465cf",
                "Number": "320684000345",
                "Pledgor": "张福斌",
                "Pawnee": "先锋基金管理有限公司",
                "PledgorAmount": "86.9061",
                "Date": "2021-11-15",
                "Status": "有效"
            },
            {
                "Eid": "0005c101a89284506b72095dba4465cf",
                "Number": "320684000113",
                "Pledgor": "施晖",
                "Pawnee": "上海建银国际投资咨询有限公司",
                "PledgorAmount": "1638.0",
                "Date": "2016-07-11",
                "Status": "无效"
            },
            {
                "Eid": "0005c101a89284506b72095dba4465cf",
                "Number": "320684000358",
                "Pledgor": "黄裕辉",
                "Pawnee": "中天国富证券有限公司",
                "PledgorAmount": "342.6939",
                "Date": "2021-12-30",
                "Status": "有效"
            },
            {
                "Eid": "0005c101a89284506b72095dba4465cf",
                "Number": "320684000116",
                "Pledgor": "周炳高",
                "Pawnee": "上海建银国际投资咨询有限公司",
                "PledgorAmount": "2433.0",
                "Date": "2016-07-11",
                "Status": "无效"
            },
            {
                "Eid": "0005c101a89284506b72095dba4465cf",
                "Number": "320684000377",
                "Pledgor": "施晖",
                "Pawnee": "泰达宏利基金管理有限公司",
                "PledgorAmount": "10.43",
                "Date": "2022-01-06",
                "Status": "有效"
            },
            {
                "Eid": "0005c101a89284506b72095dba4465cf",
                "Number": "320684000114",
                "Pledgor": "袁备",
                "Pawnee": "上海建银国际投资咨询有限公司",
                "PledgorAmount": "213.0",
                "Date": "2016-07-11",
                "Status": "无效"
            },
            {
                "Eid": "0005c101a89284506b72095dba4465cf",
                "Number": "320684000378",
                "Pledgor": "黄裕辉",
                "Pawnee": "泰达宏利基金管理有限公司",
                "PledgorAmount": "1206.5",
                "Date": "2022-01-06",
                "Status": "有效"
            },
            {
                "Eid": "0005c101a89284506b72095dba4465cf",
                "Number": "320684000118",
                "Pledgor": "徐挺",
                "Pawnee": "上海建银国际投资咨询有限公司",
                "PledgorAmount": "245.0",
                "Date": "2016-07-11",
                "Status": "无效"
            },
            {
                "Eid": "0005c101a89284506b72095dba4465cf",
                "Number": "320684000296",
                "Pledgor": "黄裕辉",
                "Pawnee": "上海骁励企业管理合伙企业（有限合伙）",
                "PledgorAmount": "1193.55",
                "Date": "2021-01-18",
                "Status": "有效"
            },
            {
                "Eid": "0005c101a89284506b72095dba4465cf",
                "Number": "320684000348",
                "Pledgor": "黄裕辉",
                "Pawnee": "中融人寿保险股份有限公司",
                "PledgorAmount": "194.0",
                "Date": "2021-11-22",
                "Status": "有效"
            },
            {
                "Eid": "0005c101a89284506b72095dba4465cf",
                "Number": "320684000301",
                "Pledgor": "袁备",
                "Pawnee": "Power Rider Enterprises Corp.",
                "PledgorAmount": "231.45",
                "Date": "2021-02-25",
                "Status": "有效"
            },
            {
                "Eid": "0005c101a89284506b72095dba4465cf",
                "Number": "320684000119",
                "Pledgor": "张福斌",
                "Pawnee": "上海建银国际投资咨询有限公司",
                "PledgorAmount": "245.0",
                "Date": "2016-07-11",
                "Status": "无效"
            },
            {
                "Eid": "0005c101a89284506b72095dba4465cf",
                "Number": "320684000347",
                "Pledgor": "施晖",
                "Pawnee": "中融人寿保险股份有限公司",
                "PledgorAmount": "398.1",
                "Date": "2021-11-22",
                "Status": "有效"
            },
            {
                "Eid": "0005c101a89284506b72095dba4465cf",
                "Number": "320684000200",
                "Pledgor": "施晖",
                "Pawnee": "陆家嘴国际信托有限公司",
                "PledgorAmount": "916.6938",
                "Date": "2017-12-27",
                "Status": "无效"
            },
            {
                "Eid": "0005c101a89284506b72095dba4465cf",
                "Number": "320684000344",
                "Pledgor": "王卫冲",
                "Pawnee": "先锋基金管理有限公司",
                "PledgorAmount": "80.9125",
                "Date": "2021-11-15",
                "Status": "有效"
            },
            {
                "Eid": "0005c101a89284506b72095dba4465cf",
                "Number": "320684000304",
                "Pledgor": "徐挺",
                "Pawnee": "Power Rider Enterprises Corp.",
                "PledgorAmount": "263.22",
                "Date": "2021-02-25",
                "Status": "有效"
            },
            {
                "Eid": "0005c101a89284506b72095dba4465cf",
                "Number": "320684000201",
                "Pledgor": "徐忠",
                "Pawnee": "招商银行股份有限公司南通分行",
                "PledgorAmount": "600.0",
                "Date": "2018-01-11",
                "Status": "无效"
            },
            {
                "Eid": "0005c101a89284506b72095dba4465cf",
                "Number": "320684000300",
                "Pledgor": "卫波",
                "Pawnee": "Power Rider Enterprises Corp.",
                "PledgorAmount": "9.08",
                "Date": "2021-02-25",
                "Status": "有效"
            }
        ]
    }
}
```

