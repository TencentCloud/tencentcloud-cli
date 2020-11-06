**Example 1: 查询客户信息**

查询指定卖场的多个客户信息

Input: 

```
tccli youmall DescribePerson --cli-unfold-argument  \
    --MallId 1 \
    --Offset 0 \
    --Limit 20
```

Output: 
```
{
    "Response": {
        "PersonSet": [
            {
                "Age": 36,
                "ArrivedCount": 16,
                "FirstArrivedTime": "2018-03-18 00:00:00",
                "Gender": 1,
                "PersonId": "78",
                "PicUrl": "",
                "Similarity": 0
            },
            {
                "Age": 28,
                "ArrivedCount": 10,
                "FirstArrivedTime": "2018-03-02 00:00:00",
                "Gender": 1,
                "PersonId": "123",
                "PicUrl": "",
                "Similarity": 0
            },
            {
                "Age": 36,
                "ArrivedCount": 16,
                "FirstArrivedTime": "2018-03-18 00:00:00",
                "Gender": 1,
                "PersonId": "362",
                "PicUrl": "",
                "Similarity": 0
            },
            {
                "Age": 24,
                "ArrivedCount": 30,
                "FirstArrivedTime": "2018-01-23 00:00:00",
                "Gender": 2,
                "PersonId": "467",
                "PicUrl": "",
                "Similarity": 0
            },
            {
                "Age": 20,
                "ArrivedCount": 1,
                "FirstArrivedTime": "2018-09-06 14:40:33",
                "Gender": 1,
                "PersonId": "362347623",
                "PicUrl": "",
                "Similarity": 0
            },
            {
                "Age": 22,
                "ArrivedCount": 1,
                "FirstArrivedTime": "2018-09-18 17:06:08",
                "Gender": 1,
                "PersonId": "393731663149746",
                "PicUrl": "",
                "Similarity": 0
            },
            {
                "Age": 24,
                "ArrivedCount": 1,
                "FirstArrivedTime": "2018-09-14 17:31:52",
                "Gender": 2,
                "PersonId": "2645250752598047",
                "PicUrl": "",
                "Similarity": 0
            },
            {
                "Age": 21,
                "ArrivedCount": 1,
                "FirstArrivedTime": "2018-09-14 12:58:48",
                "Gender": 1,
                "PersonId": "10526545872139612",
                "PicUrl": "",
                "Similarity": 0
            },
            {
                "Age": 19,
                "ArrivedCount": 1,
                "FirstArrivedTime": "2018-09-14 17:31:54",
                "Gender": 2,
                "PersonId": "11652450007324432",
                "PicUrl": "",
                "Similarity": 0
            },
            {
                "Age": 28,
                "ArrivedCount": 1,
                "FirstArrivedTime": "2018-10-02 09:34:07",
                "Gender": 2,
                "PersonId": "18408230188136202",
                "PicUrl": "",
                "Similarity": 0
            },
            {
                "Age": 32,
                "ArrivedCount": 1,
                "FirstArrivedTime": "2018-10-02 09:34:07",
                "Gender": 2,
                "PersonId": "21785929908663282",
                "PicUrl": "",
                "Similarity": 0
            },
            {
                "Age": 22,
                "ArrivedCount": 1,
                "FirstArrivedTime": "2018-09-29 11:53:10",
                "Gender": 2,
                "PersonId": "24037629746704827",
                "PicUrl": "",
                "Similarity": 0
            },
            {
                "Age": 34,
                "ArrivedCount": 1,
                "FirstArrivedTime": "2018-09-14 12:59:00",
                "Gender": 2,
                "PersonId": "30792744195306845",
                "PicUrl": "",
                "Similarity": 0
            },
            {
                "Age": 35,
                "ArrivedCount": 1,
                "FirstArrivedTime": "2018-10-02 09:34:07",
                "Gender": 2,
                "PersonId": "31919029070242542",
                "PicUrl": "",
                "Similarity": 0
            },
            {
                "Age": 35,
                "ArrivedCount": 1,
                "FirstArrivedTime": "2018-09-13 14:13:48",
                "Gender": 1,
                "PersonId": "33044528809806896",
                "PicUrl": "",
                "Similarity": 0
            },
            {
                "Age": 28,
                "ArrivedCount": 1,
                "FirstArrivedTime": "2018-10-02 09:34:07",
                "Gender": 2,
                "PersonId": "33044928977089521",
                "PicUrl": "",
                "Similarity": 0
            },
            {
                "Age": 46,
                "ArrivedCount": 1,
                "FirstArrivedTime": "2018-10-02 09:34:07",
                "Gender": 2,
                "PersonId": "35296728790776086",
                "PicUrl": "",
                "Similarity": 0
            },
            {
                "Age": 20,
                "ArrivedCount": 1,
                "FirstArrivedTime": "2018-09-13 20:27:19",
                "Gender": 2,
                "PersonId": "36422228530328097",
                "PicUrl": "",
                "Similarity": 0
            },
            {
                "Age": 24,
                "ArrivedCount": 1,
                "FirstArrivedTime": "2018-10-02 09:34:07",
                "Gender": 1,
                "PersonId": "37548528650778933",
                "PicUrl": "",
                "Similarity": 0
            },
            {
                "Age": 33,
                "ArrivedCount": 1,
                "FirstArrivedTime": "2018-10-02 09:34:07",
                "Gender": 1,
                "PersonId": "38674428511297514",
                "PicUrl": "",
                "Similarity": 0
            }
        ],
        "RequestId": "zephyryi-1538448929679252515",
        "TotalCount": 10029
    }
}
```

