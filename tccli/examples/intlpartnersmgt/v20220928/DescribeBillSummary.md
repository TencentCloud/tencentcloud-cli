**Example 1: DescribeBillSummary 标签维度统计**

该示例用于子客计费中心L1账单的api, tag维度统计

POST / HTTP/1.1
Host: intlpartnersmgt.tencentcloudapi.com
Content-Type: application/json
X-TC-Action: DescribeBillSummary
<公共请求参数>

Input: 

```
tccli intlpartnersmgt DescribeBillSummary --cli-unfold-argument  \
    --Month 2023-10 \
    --GroupType tag \
    --TagKey dev_tag_key
```

Output: 
```
{
    "Response": {
        "SummaryDetail": [
            {
                "Business": [
                    {
                        "BusinessCodeName": "CVM Dedicated Host",
                        "BusinessCode": "p_cdh",
                        "OriginalCost": "12.11",
                        "VoucherPayAmount": "1.1",
                        "RICost": "0.1",
                        "TotalCost": "12.1"
                    }
                ],
                "OriginalCost": "12.1",
                "VoucherPayAmount": "1.1",
                "RICost": "1.1",
                "TotalCost": "2.2",
                "GroupKey": "dev_tag_key",
                "GroupValue": "default"
            }
        ],
        "RequestId": "abc"
    }
}
```

**Example 2: DescribeBillSummary 项目维度统计**

该示例用于子客计费中心L1账单的api, project维度统计

POST / HTTP/1.1
Host: intlpartnersmgt.tencentcloudapi.com
Content-Type: application/json
X-TC-Action: DescribeBillSummary
<公共请求参数>

Input: 

```
tccli intlpartnersmgt DescribeBillSummary --cli-unfold-argument  \
    --Month 2023-10 \
    --GroupType project
```

Output: 
```
{
    "Response": {
        "SummaryDetail": [
            {
                "Business": [
                    {
                        "BusinessCodeName": "cloud block storage",
                        "BusinessCode": "p_cbs",
                        "OriginalCost": "148.40000000",
                        "VoucherPayAmount": "129.70000000",
                        "RICost": "0.00000000",
                        "TotalCost": "18.70000000"
                    }
                ],
                "OriginalCost": "148.40000000",
                "VoucherPayAmount": "129.70000000",
                "RICost": "0.00000000",
                "TotalCost": "18.70000000",
                "GroupKey": "0",
                "GroupValue": "default"
            }
        ],
        "RequestId": "abc"
    }
}
```

**Example 3: DescribeBillSummary 产品维度统计**

该示例用于子客计费中心L1账单的api, product维度统计

POST / HTTP/1.1
Host: intlpartnersmgt.tencentcloudapi.com
Content-Type: application/json
X-TC-Action: DescribeBillSummary
<公共请求参数>

Input: 

```
tccli intlpartnersmgt DescribeBillSummary --cli-unfold-argument  \
    --Month 2023-10 \
    --GroupType product
```

Output: 
```
{
    "Response": {
        "SummaryDetail": [
            {
                "Business": null,
                "OriginalCost": "148.40000000",
                "VoucherPayAmount": "129.70000000",
                "RICost": "0.00000000",
                "TotalCost": "18.70000000",
                "GroupKey": "p_cbs",
                "GroupValue": "cloud block storage"
            }
        ],
        "RequestId": "abc"
    }
}
```

