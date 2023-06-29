**Example 1: DescribeChangeRecords1**

DescribeChangeRecords1

Input: 

```
tccli eportrait DescribeChangeRecords --cli-unfold-argument  \
    --Limit 10 \
    --Offset 0 \
    --Eid d19588af77665b32b1db3977e2428123
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "AfterContent": "武汉市江夏区腾讯大道特1号",
                "BeforeContent": "武汉市江夏经济开发区庙山阳光五路特1号",
                "ChangeDate": "2018-04-18",
                "ChangeItem": "地址变更（住所地址、经营场所、驻在地址等变更）",
                "Eid": "d19588af77665b32b1db3977e2428123",
                "Type": "地址变更"
            },
            {
                "AfterContent": "沈丹",
                "BeforeContent": "陈一丹",
                "ChangeDate": "2017-12-28",
                "ChangeItem": "负责人变更（法定代表人、负责人、首席代表、合伙事务执行人等变更）",
                "Eid": "d19588af77665b32b1db3977e2428123",
                "Type": "法定代表人变更"
            },
            {
                "AfterContent": "许晨晔（监事）、马化腾（董事）、Charles St Leger Searle（董事）、沈丹（董事长兼总经理）",
                "BeforeContent": "陈一丹（董事长兼总经理）、许晨晔（监事）、马化腾（董事）、Charles St Leger Searle（董事）",
                "ChangeDate": "2017-12-28",
                "ChangeItem": "高级管理人员备案（董事、监事、经理等）",
                "Eid": "d19588af77665b32b1db3977e2428123",
                "Type": "主要人员变更"
            },
            {
                "AfterContent": "从事计算机软硬件的技术开发；销售自行开发的软件；计算机技术服务；自有房屋租赁；停车场管理服务；房屋维修；物业管理。(上述经营范围不涉及外商投资准入特别管理措施)（依法须经审批的项目，经相关部门审批后方可开展经营活动）",
                "BeforeContent": "计算机软硬件的技术开发及销售、计算机技术及信息服务。(上述经营范围中国家有专项规定需经审批的项目，经审批后或凭有效许可证方可经营)",
                "ChangeDate": "2017-12-28",
                "ChangeItem": "经营范围变更（含业务范围变更）",
                "Eid": "d19588af77665b32b1db3977e2428123",
                "Type": "经营范围变更"
            },
            {
                "AfterContent": "许晨晔（监事）、马化腾（董事）、Charles St Leger Searle（董事）、沈丹（董事长兼总经理）",
                "BeforeContent": "陈一丹（董事长兼总经理）、许晨晔（监事）、马化腾（董事）、Charles St Leger Searle（董事）",
                "ChangeDate": "2017-12-28",
                "ChangeItem": "投资人变更（包括出资额、出资方式、出资日期、投资人名称等）",
                "Eid": "d19588af77665b32b1db3977e2428123",
                "Type": "股东信息变更"
            },
            {
                "AfterContent": "3000.0",
                "BeforeContent": "0.0",
                "ChangeDate": "2012-01-13",
                "ChangeItem": "实收资本变更",
                "Eid": "d19588af77665b32b1db3977e2428123",
                "Type": ""
            },
            {
                "AfterContent": "中霸集团有限公司（100.0%）（3000.0，100.0%，现金,3000.0） 2012-05-18 ；",
                "BeforeContent": "中霸集团有限公司（100.0%）（3000.0，100.0%，现金,0.0） 2012-05-18 ；",
                "ChangeDate": "2012-01-13",
                "ChangeItem": "投资人变更（包括出资额、出资方式、出资日期、投资人名称等）",
                "Eid": "d19588af77665b32b1db3977e2428123",
                "Type": "股东信息变更"
            },
            {
                "AfterContent": "陈一丹，许晨晔，马化腾，Charles St Leger Searle",
                "BeforeContent": "陈一丹，许晨晔，马化腾，任宇昕，Charles St Leger Searle",
                "ChangeDate": "2016-10-24",
                "ChangeItem": "高级管理人员备案（董事、监事、经理等）",
                "Eid": "d19588af77665b32b1db3977e2428123",
                "Type": "主要人员变更"
            },
            {
                "AfterContent": "陈一丹，许晨晔，马化腾，Charles St Leger Searle",
                "BeforeContent": "陈一丹，许晨晔，马化腾，任宇昕，Charles St Leger Searle",
                "ChangeDate": "2016-10-24",
                "ChangeItem": "投资人变更（包括出资额、出资方式、出资日期、投资人名称等）",
                "Eid": "d19588af77665b32b1db3977e2428123",
                "Type": "股东信息变更"
            },
            {
                "AfterContent": "证件号码:*; 姓名：陈一丹 职务：董事长/总经理;证件号码:*; 姓名：许晨晔 职务：监事;证件号码:*; 姓名：马化腾 职务：董事;证件号码:*; 姓名：任宇昕 职务：董事;证件号码:*;8） 姓名：Charles St Leger Searle 职务：董事;",
                "BeforeContent": "证件号码:*; 姓名：陈一丹 职务：董事长/总经理;证件号码:*; 姓名：许晨晔 职务：监事;证件号码:*; 姓名：张志东 职务：董事;证件号码:*; 姓名：马化腾 职务：董事;证件号码:*;8） 姓名：Charles St Leger Searle 职务：董事;",
                "ChangeDate": "2015-04-01",
                "ChangeItem": "投资人变更（包括出资额、出资方式、出资日期、投资人名称等）",
                "Eid": "d19588af77665b32b1db3977e2428123",
                "Type": "股东信息变更"
            }
        ],
        "RequestId": "e9bc908a-d5c1-486c-84e6-17c3c080ec50",
        "TotalCount": 12
    }
}
```

