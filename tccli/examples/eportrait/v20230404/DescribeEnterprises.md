**Example 1: DescribeEnterprises5**

DescribeEnterprises5

Input: 

```
tccli eportrait DescribeEnterprises --cli-unfold-argument  \
    --Name 腾讯科技 \
    --Offset 0 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "Address": "广州市天河区华景路1号6楼",
                "EconKind": "分公司",
                "Eid": "1e8a14099e08bd9cb930e052abb186f5",
                "Email": "",
                "Name": "腾讯科技（深圳）有限公司广州分公司",
                "NewStatusCode": "2",
                "OperName": "胡仁杰",
                "RegistCap": null,
                "Score": 100,
                "StartDate": "2003-12-29",
                "Telephone": "81167888"
            },
            {
                "Address": "吉林省镇赉县坦途镇信用社西第五家",
                "EconKind": "个体工商户",
                "Eid": "32c309f6f6185958b9c1c8f30241df1d",
                "Email": "",
                "Name": "镇赉县坦途镇腾讯科技手机店",
                "NewStatusCode": "1",
                "OperName": "刘国祥",
                "RegistCap": null,
                "Score": 100,
                "StartDate": "2013-11-12",
                "Telephone": ""
            },
            {
                "Address": "北京市朝阳区北辰东路8号汇宾大厦A910室",
                "EconKind": "外国(地区)企业常驻代表机构",
                "Eid": "59be2c16f365c908ff277de37eecb303",
                "Email": null,
                "Name": "香港腾讯科技亚太有限公司北京代表处",
                "NewStatusCode": "2",
                "OperName": "刘选忠",
                "RegistCap": null,
                "Score": 100,
                "StartDate": "1999-08-20",
                "Telephone": null
            },
            {
                "Address": "新安县新城新华书店东侧988号",
                "EconKind": "个体工商户",
                "Eid": "87e27c1960399bba275a618f2d09e267",
                "Email": "",
                "Name": "新安县新城腾讯科技电脑城",
                "NewStatusCode": "2",
                "OperName": "高园园",
                "RegistCap": null,
                "Score": 100,
                "StartDate": "2015-05-20",
                "Telephone": "18037901770"
            },
            {
                "Address": "北京市海淀区海淀大街甲36号办公楼B08室",
                "EconKind": "有限责任公司(自然人投资或控股)",
                "Eid": "892e53c6b437f52d5fa961df84d2952f",
                "Email": null,
                "Name": "北京金腾讯科技有限公司",
                "NewStatusCode": "3",
                "OperName": "赵菊花",
                "RegistCap": "10万",
                "Score": 100,
                "StartDate": "2003-08-22",
                "Telephone": null
            },
            {
                "Address": "贵州省黔东南苗族侗族自治州台江县施洞镇清江村方寨一组",
                "EconKind": "个体工商户",
                "Eid": "bb28a1a7a34567b7126de83a97d05091",
                "Email": null,
                "Name": "台江县施洞镇腾讯科技代理点",
                "NewStatusCode": "1",
                "OperName": "张小春",
                "RegistCap": null,
                "Score": 100,
                "StartDate": "2016-12-12",
                "Telephone": "18508551549"
            }
        ],
        "RequestId": "f7d8b3f0-e468-410a-a97f-5fde2bd90616",
        "TotalCount": 6
    }
}
```

