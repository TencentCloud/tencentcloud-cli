**Example 1: 查询溯源信息**

查询某个批次的溯源信息

Input: 

```
tccli trp DescribeTraceDataList --cli-unfold-argument  \
    --BatchId xfetmgoiky2nms6nk8 \
    --Code 
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "TraceDataList": [
            {
                "TraceId": "1mO3n3W0LDhAaADGwHjj3",
                "TraceItems": [
                    {
                        "Key": "name",
                        "Name": "名称",
                        "Value": "xltest",
                        "Type": "text",
                        "ReadOnly": true,
                        "Hidden": false,
                        "Values": [],
                        "Ext": "",
                        "Attrs": [],
                        "List": []
                    },
                    {
                        "Key": "avatar",
                        "Name": "主图",
                        "Value": "",
                        "Type": "image",
                        "ReadOnly": false,
                        "Hidden": false,
                        "Values": [
                            "https://webcdn.m.qq.com/anxin/public/4054d20b71d30db847492eecc8057e90.jpg"
                        ],
                        "Ext": "",
                        "Attrs": [],
                        "List": []
                    },
                    {
                        "Key": "message",
                        "Name": "提示文本",
                        "Value": "商品信息溯源详情",
                        "Type": "text",
                        "ReadOnly": false,
                        "Hidden": false,
                        "Values": [],
                        "Ext": "",
                        "Attrs": [],
                        "List": []
                    },
                    {
                        "Key": "desc",
                        "Name": "卡片描述",
                        "Value": "二维码已完成扫码，请查看信息",
                        "Type": "text",
                        "ReadOnly": false,
                        "Hidden": false,
                        "Values": [],
                        "Ext": "",
                        "Attrs": [],
                        "List": []
                    }
                ],
                "PhaseName": "设计阶段",
                "PhaseData": {
                    "AppId": "",
                    "AppName": "",
                    "AppPath": "",
                    "HeadEnabled": false,
                    "HeadTitle": "",
                    "Key": ""
                },
                "Status": 1,
                "Rank": 1,
                "Type": 1,
                "Code": "https://anxin.qq.com/q99j9ovp5c6sok7l5g",
                "Phase": 2,
                "TraceTime": "2024-10-30T07:16:21.265Z",
                "CreateTime": "2024-10-30T07:16:21.265Z",
                "ChainStatus": 1,
                "ChainTime": "2024-10-30T07:16:21.265Z",
                "ChainData": {
                    "BlockTime": "2024-03-27T03:33:21.000Z",
                    "BlockHash": "129fd196158b497b88bcb02ac7b34f3729c806e925074b448bad35f3da960072",
                    "BlockHeight": "684"
                },
                "CorpId": 10000
            }
        ],
        "RequestId": "abc"
    }
}
```

