**Example 1: 获取内容风险列表**

获取内容风险列表

Input: 

```
tccli csip DescribeRiskCenterWebsiteRiskList --cli-unfold-argument  \
    --MemberId mem-68b8087a65268000 mem-tencent-522badef8ad96a4d \
    --Filter.Limit 10 \
    --Filter.Offset 1
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "AffectAsset": "1.1.1.1",
                "Level": "high",
                "RecentTime": "2022-10-10 00:00:00",
                "FirstTime": "2022-10-10 00:00:00",
                "Status": 0,
                "Id": "id-wq142",
                "Index": "index-33wrt",
                "InstanceId": "ins-******",
                "InstanceName": "instance name",
                "AppId": "130********",
                "Nick": "nickname",
                "Uin": "100*********",
                "URL": "http://example.com",
                "URLPath": "url*******",
                "InstanceType": "CVM",
                "DetectEngine": "engine1",
                "ResultDescribe": "result info",
                "SourceURL": "http://example.com",
                "SourceURLPath": "path"
            }
        ],
        "DetectEngineLists": [
            {
                "Text": "vss",
                "Value": "vss"
            }
        ],
        "InstanceTypeLists": [
            {
                "Text": "托管集群",
                "Value": "managed_cluster"
            },
            {
                "Text": "CVM",
                "Value": "CVM"
            },
            {
                "Text": "本地镜像",
                "Value": "Local"
            },
            {
                "Text": "CLB",
                "Value": "CLB"
            }
        ],
        "LevelLists": [
            {
                "Text": "严重",
                "Value": "extreme"
            },
            {
                "Text": "高危",
                "Value": "high"
            },
            {
                "Text": "中危",
                "Value": "middle"
            },
            {
                "Text": "低危",
                "Value": "low"
            },
            {
                "Text": "提示",
                "Value": "info"
            }
        ],
        "RequestId": "6fcf6762-9729-49c4-8bbd-7812ecdca062",
        "StatusLists": [
            {
                "Text": "已忽略",
                "Value": "2"
            },
            {
                "Text": "已封禁",
                "Value": "3"
            },
            {
                "Text": "未处理",
                "Value": "0"
            },
            {
                "Text": "已处置",
                "Value": "1"
            }
        ],
        "TotalCount": 0
    }
}
```

