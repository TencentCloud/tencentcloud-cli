**Example 1: 查询数据集列表**



Input: 

```
tccli tsf DescribePrograms --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "865be0aa-ae4d-443a-bb72-01995d1f5f4e",
        "Result": {
            "TotalCount": 5,
            "Content": [
                {
                    "ProgramId": "program-96a79v5b",
                    "ProgramName": "AUTO-appId-@ALL@",
                    "ProgramDesc": null,
                    "CreationTime": 1542870362,
                    "LastUpdateTime": 1542870362,
                    "DeleteFlag": false,
                    "ProgramItemList": null
                },
                {
                    "ProgramId": "program-a79e9j9v",
                    "ProgramName": "测试数据集",
                    "ProgramDesc": null,
                    "CreationTime": 1566467701,
                    "LastUpdateTime": 1566467701,
                    "DeleteFlag": true,
                    "ProgramItemList": null
                },
                {
                    "ProgramId": "program-l6ymbvgd",
                    "ProgramName": "AUTO-NOTHING",
                    "ProgramDesc": null,
                    "CreationTime": 1542870362,
                    "LastUpdateTime": 1542870362,
                    "DeleteFlag": true,
                    "ProgramItemList": null
                },
                {
                    "ProgramId": "program-ymqbq8bv",
                    "ProgramName": "测试数据集9",
                    "ProgramDesc": "测试数据集desc9",
                    "CreationTime": 1566467729,
                    "LastUpdateTime": 1566483895,
                    "DeleteFlag": false,
                    "ProgramItemList": null
                },
                {
                    "ProgramId": "program-yn2g3e9y",
                    "ProgramName": "测试数据集3",
                    "ProgramDesc": "测试数据集desc",
                    "CreationTime": 1566479755,
                    "LastUpdateTime": 1566479755,
                    "DeleteFlag": false,
                    "ProgramItemList": null
                }
            ]
        }
    }
}
```

