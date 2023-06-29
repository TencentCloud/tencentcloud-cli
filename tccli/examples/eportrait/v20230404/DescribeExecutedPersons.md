**Example 1: 查询企业被执行人列表**

查询企业被执行人列表

Input: 

```
tccli eportrait DescribeExecutedPersons --cli-unfold-argument  \
    --Limit 12 \
    --Offset 0 \
    --Eid 2a83acf0a132edaae1b20be2899b9fcb
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "Amount": "15266827",
                "CaseDate": "2014-01-03",
                "CaseNumber": "(2014)厦执行字第44号",
                "Court": "厦门市中级人民法院",
                "Eid": "2a83acf0a132edaae1b20be2899b9fcb",
                "Ename": "厦门市新阳隆汽车销售有限公司",
                "Status": "0"
            },
            {
                "Amount": "86701048",
                "CaseDate": "2014-10-14",
                "CaseNumber": "(2014)厦执行字第734号",
                "Court": "厦门市中级人民法院",
                "Eid": "2a83acf0a132edaae1b20be2899b9fcb",
                "Ename": "厦门市新阳隆汽车销售有限公司",
                "Status": "0"
            },
            {
                "Amount": "15724251",
                "CaseDate": "2016-02-23",
                "CaseNumber": "(2016)闽02执137号",
                "Court": "厦门市中级人民法院",
                "Eid": "2a83acf0a132edaae1b20be2899b9fcb",
                "Ename": "厦门市新阳隆汽车销售有限公司",
                "Status": "0"
            },
            {
                "Amount": "6060000",
                "CaseDate": "2017-04-13",
                "CaseNumber": "(2017)闽0203执2377号",
                "Court": "厦门市思明区人民法院",
                "Eid": "2a83acf0a132edaae1b20be2899b9fcb",
                "Ename": "厦门市新阳隆汽车销售有限公司",
                "Status": "0"
            },
            {
                "Amount": "7053869",
                "CaseDate": "2014-01-03",
                "CaseNumber": "(2014)厦执行字第45号",
                "Court": "厦门市中级人民法院",
                "Eid": "2a83acf0a132edaae1b20be2899b9fcb",
                "Ename": "厦门市新阳隆汽车销售有限公司",
                "Status": "0"
            },
            {
                "Amount": "10034667",
                "CaseDate": "2016-07-08",
                "CaseNumber": "(2016)闽02执542号",
                "Court": "厦门市中级人民法院",
                "Eid": "2a83acf0a132edaae1b20be2899b9fcb",
                "Ename": "厦门市新阳隆汽车销售有限公司",
                "Status": "0"
            },
            {
                "Amount": "23352000",
                "CaseDate": "2015-03-12",
                "CaseNumber": "(2015)厦执字第281号",
                "Court": "厦门市中级人民法院",
                "Eid": "2a83acf0a132edaae1b20be2899b9fcb",
                "Ename": "厦门市新阳隆汽车销售有限公司",
                "Status": "0"
            },
            {
                "Amount": "10020928",
                "CaseDate": "2016-07-08",
                "CaseNumber": "(2016)闽02执543号",
                "Court": "厦门市中级人民法院",
                "Eid": "2a83acf0a132edaae1b20be2899b9fcb",
                "Ename": "厦门市新阳隆汽车销售有限公司",
                "Status": "0"
            },
            {
                "Amount": "24355640",
                "CaseDate": "2017-08-30",
                "CaseNumber": "(2017)闽02执654号",
                "Court": "厦门市中级人民法院",
                "Eid": "2a83acf0a132edaae1b20be2899b9fcb",
                "Ename": "厦门市新阳隆汽车销售有限公司",
                "Status": "0"
            },
            {
                "Amount": "1126.23",
                "CaseDate": "2013-05-07",
                "CaseNumber": "(2013)同法执字第01065号",
                "Court": "厦门市同安区人民法院",
                "Eid": "2a83acf0a132edaae1b20be2899b9fcb",
                "Ename": "厦门市新阳隆汽车销售有限公司",
                "Status": null
            },
            {
                "Amount": "3000000",
                "CaseDate": "2013-08-27",
                "CaseNumber": "(2013)厦执行字第00675号",
                "Court": "厦门市中级人民法院",
                "Eid": "2a83acf0a132edaae1b20be2899b9fcb",
                "Ename": "厦门市新阳隆汽车销售有限公司",
                "Status": null
            },
            {
                "Amount": "7100000",
                "CaseDate": "2014-03-26",
                "CaseNumber": "(2014)厦执行字第00249号",
                "Court": "厦门市中级人民法院",
                "Eid": "2a83acf0a132edaae1b20be2899b9fcb",
                "Ename": "厦门市新阳隆汽车销售有限公司",
                "Status": null
            }
        ],
        "RequestId": "462be07e-e649-4c9e-9ba1-5b80fe6123cc",
        "TotalCount": 45
    }
}
```

