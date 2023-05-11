**Example 1: DescribeMappingResults**



Input: 

```
tccli ssa DescribeMappingResults --cli-unfold-argument  \
    --Filter.0.Filter.0.FilterValue ins-3u7e8ki2 \
    --Filter.0.Filter.0.FilterOperatorType 1 \
    --Filter.0.Filter.0.FilterKey AssetId \
    --Filter.0.Logic 1 \
    --PageIndex 1 \
    --PageSize 1 \
    --Sorter.0.SortType 1 \
    --Sorter.0.SortKey LastMappingTime
```

Output: 
```
{
    "Response": {
        "Data": {
            "TaskMaxCount": 2,
            "TaskCount": 0,
            "Statistics": [
                {
                    "AssetCount": 1,
                    "AssetType": "cvm"
                }
            ],
            "Result": [
                {
                    "Component": "OpenSSH",
                    "Protocol": "TCP",
                    "DisposalRecommendations": "限制访问",
                    "DisposalRecommendation": 2,
                    "SecurityStatus": [
                        {},
                        {}
                    ],
                    "Region": "ap-guangzhou",
                    "Port": "22",
                    "AssetType": "cvm",
                    "MappingStatus": 2,
                    "LastMappingTime": "2022-04-08 02:35:00",
                    "PrivateIp": "172.16.16.29",
                    "Domain": "22",
                    "AssetId": "ins-3u7e8ki2",
                    "Process": "sshd",
                    "Service": "ssh",
                    "AssetIp": "106.55.242.82",
                    "OS": "CentOS 7.7 64位",
                    "DisposalRecommendationDetails": "<li>1、通知业务方说明端口互联网暴露的必要性和需要面向哪些场景暴露</li><li>2、如果是业务端口，需要确保建议的安全防护均已具备</li><li>3、如果是远程运维用端口，应能关则关，改为使用堡垒机等手段运维。</li><li>4、如果是必须开放的端口，尽可能配置安全组入站规则或使用 <a target=\"_blank\" rel=\"noreferrer\" href=\"https://console.cloud.tencent.com/cfw/ac/auth?tab=user\">云防火墙微信远程运维</a> 来对端口访问做控制</li><li>5、无法关闭的端口，需要检查安全防护状态，尽可能保证所有建议的安全防护均已具备</li><li>6、可鼠标悬浮安全防护状态查看具体说明和建议</li>",
                    "AssetName": "数据安全组virustotal检测6"
                }
            ]
        },
        "Total": 1,
        "RequestId": "fd1ed4b0-5534-406d-a2ff-cdf486536761"
    }
}
```

