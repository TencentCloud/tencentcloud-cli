**Example 1: 查询cos数据识别结果列表**



Input: 

```
tccli csip DescribeCosIdentifyFileList --cli-unfold-argument  \
    --BucketName brainzhao-test-1302396215 \
    --MemberId mem-68b8087a65268000
```

Output: 
```
{
    "Response": {
        "DataSet": [
            {
                "CategoryDetails": [
                    {
                        "CategoryId": 356,
                        "CategoryName": "个人信息",
                        "RuleSet": [
                            {
                                "LevelId": 10,
                                "LevelName": "一般",
                                "LevelScore": 1,
                                "RuleId": 5813,
                                "RuleName": "车牌号码"
                            }
                        ]
                    }
                ],
                "DirName": "",
                "FileName": "Sensitive_data_data.csv"
            }
        ],
        "TotalCount": 2,
        "RequestId": "e0a254a4-18d5-4c7c-9766-23ed2e790925"
    }
}
```

