**Example 1: 获取合同智能提取任务详情**



Input: 

```
tccli ess DescribeInformationExtractionTask --cli-unfold-argument  \
    --Operator.UserId yDx************************xxx \
    --TaskId yDx************************yyy
```

Output: 
```
{
    "Response": {
        "Fields": [
            {
                "Name": "甲方",
                "Values": [
                    "张三",
                    "李四"
                ],
                "Type": "Text",
                "Description": "提取甲方信息"
            }
        ],
        "Status": 3,
        "Url": "https://file.ess.tencent.cn/bresource/resource/resource/0/0.XLSX?hkey=c83cf852247f9075f675f350e6d6ebeda61fa2d74d136f8efccdde201dc72cb280dcd8992c91808c55817c57c4bf87f718adfa54bf152500e9a45beb6cc9f697a0c938dc46f2abe3288a77d1fddf145d4cd2027ed8e4b6030b2f95355be37221",
        "RequestId": "s1735294966632123121"
    }
}
```

