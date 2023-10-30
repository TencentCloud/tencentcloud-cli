**Example 1: 批量获取下载链接一个成功一个失败**

批量获取2个合同流程的下载链接, 因第一个合同yDwivUUckpor6wtoUuogwQHCAB0ES0p1不存在, 第二个合同获取成功

Input: 

```
tccli essbasic DescribeResourceUrlsByFlows --cli-unfold-argument  \
    --Agent.AppId yDwhxUUckp3gl8j5UuFX33LSNozpRsbi \
    --Agent.ProxyOrganizationOpenId org_dianziqian \
    --Agent.ProxyOperator.OpenId n9527 \
    --Agent.ProxyAppId  \
    --FlowIds yDwivUUckpor6wtoUuogwQHCAB0ES0p1 yDwi8UUckpo5fz9cUqI6nGwcuTvt9YSh
```

Output: 
```
{
    "Response": {
        "FlowResourceUrlInfos": [
            {
                "FlowId": "yDwivUUckpor6wtoUuogwQHCAB0ES0p1",
                "ResourceUrlInfos": []
            },
            {
                "FlowId": "yDwi8UUckpo5fz9cUqI6nGwcuTvt9YSh",
                "ResourceUrlInfos": [
                    {
                        "Url": "https://file.test.ess.tencent.cn/file/FLOW/yDwi8UUckpo5fz9cUqI6nGwcuTvt9YSh/0/0.PDF?hkey=70b1***9c63",
                        "Name": "合同,250151025185515.pdf",
                        "Type": "PDF"
                    }
                ]
            }
        ],
        "ErrorMessages": [
            "查询流程不存在",
            ""
        ],
        "RequestId": "2e9fc432-53b4-4286-b706-7a5de509310b"
    }
}
```

**Example 2: 批量获取下载链接全成功**

批量获取2个合同流程全部成功

Input: 

```
tccli essbasic DescribeResourceUrlsByFlows --cli-unfold-argument  \
    --Agent.AppId yDwhxUUckp3gl8j5UuFX33LSNozpRsbi \
    --Agent.ProxyOrganizationOpenId org_dianziqian \
    --Agent.ProxyOperator.OpenId n9527 \
    --Agent.ProxyAppId  \
    --FlowIds yDwivUUckpor6wtoUuogwQHCAB0ES0pQ yDwi8UUckpo5fz9cUqI6nGwcuTvt9YSh
```

Output: 
```
{
    "Response": {
        "FlowResourceUrlInfos": [
            {
                "FlowId": "yDwivUUckpor6wtoUuogwQHCAB0ES0pQ",
                "ResourceUrlInfos": [
                    {
                        "Url": "https://file.test.ess.tencent.cn/file/FLOW/yDwivUUckpor6wtoUuogwQHCAB0ES0pQ/0/0.PDF?hkey=70b1**9c63e",
                        "Name": "合同,270481027143248.pdf",
                        "Type": "PDF"
                    }
                ]
            },
            {
                "FlowId": "yDwi8UUckpo5fz9cUqI6nGwcuTvt9YSh",
                "ResourceUrlInfos": [
                    {
                        "Url": "https://file.test.ess.tencent.cn/file/FLOW/yDwi8UUckpo5fz9cUqI6nGwcuTvt9YSh/0/0.PDF?hkey=70b1**c63",
                        "Name": "合同,250151025185515.pdf",
                        "Type": "PDF"
                    }
                ]
            }
        ],
        "ErrorMessages": [
            "",
            ""
        ],
        "RequestId": "d49c0838-94b6-45f8-995e-42f61dfa0c05"
    }
}
```

