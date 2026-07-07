**Example 1: 识别字段Top5**



Input: 

```
tccli csip DescribeDspmIdentifyDistributionStatistics --cli-unfold-argument  \
    --StatType FieldTop5Asset \
    --MemberId mem-12df23ed \
    --AssetType cdb \
    --ComplianceId 9050
```

Output: 
```
{
    "Response": {
        "DataSet": [
            {
                "Name": "cdb-3gxg132h(cdb108345385)",
                "Value": 12
            }
        ],
        "RequestId": "880ac5c4-1b9b-410e-a7da-5c73b27ea44c"
    }
}
```

**Example 2: 识别字段分类分布**



Input: 

```
tccli csip DescribeDspmIdentifyDistributionStatistics --cli-unfold-argument  \
    --StatType FieldCategoryDistribution \
    --MemberId mem-12df23ed \
    --AssetType cdb \
    --ComplianceId 9050
```

Output: 
```
{
    "Response": {
        "DataSet": [
            {
                "Name": "个人敏感信息",
                "Value": 3
            }
        ],
        "RequestId": "11effbc0-20fb-48b6-82fc-de389e02e909"
    }
}
```

**Example 3: 识别字段分级分布**



Input: 

```
tccli csip DescribeDspmIdentifyDistributionStatistics --cli-unfold-argument  \
    --StatType FieldLevelDistribution \
    --MemberId mem-12df23ed \
    --AssetType cdb \
    --ComplianceId 9050
```

Output: 
```
{
    "Response": {
        "DataSet": [
            {
                "Name": "敏感",
                "Value": 3
            }
        ],
        "RequestId": "644f3941-09ce-405f-ae28-398ba4343d56"
    }
}
```

**Example 4: 识别资产分布**



Input: 

```
tccli csip DescribeDspmIdentifyDistributionStatistics --cli-unfold-argument  \
    --StatType AssetDistribution \
    --MemberId mem-12df23ed \
    --AssetType cdb \
    --ComplianceId 9050
```

Output: 
```
{
    "Response": {
        "DataSet": [
            {
                "Name": "AssetNum",
                "Value": 1
            }
        ],
        "RequestId": "b7e6e036-d7ed-4ae3-8ead-6f74a3bd133a"
    }
}
```

